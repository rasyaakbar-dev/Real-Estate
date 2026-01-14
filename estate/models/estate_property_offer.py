from datetime import timedelta

from odoo import api, fields, models
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    # Private attributes
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = "price desc"
    _sql_constraints = [
        (
            "check_price",
            "CHECK(price > 0)",
            "The offer price must be strictly positive",
        ),
    ]

    # Field declarations
    price = fields.Float(required=True)
    status = fields.Selection(
        selection=[("accepted", "Accepted"), ("refused", "Refused")],
        copy=False,
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    property_type_id = fields.Many2one(
        "estate.property.type", related="property_id.property_type_id", store=True
    )
    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(
        string="Deadline",
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
    )

    # Compute and inverse methods
    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for record in self:
            if record.validity and record.create_date:
                record.date_deadline = record.create_date + timedelta(
                    days=record.validity
                )

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline and record.create_date:
                record.validity = (
                    record.date_deadline - record.create_date.date()
                ).days

    # CRUD methods
    @api.model
    def create(self, vals):
        offer = super().create(vals)
        if offer.property_id.state == "new":
            offer.property_id.state = "offer_received"
        return offer

    # Action methods
    def action_accept(self):
        for record in self:
            if record.property_id.offer_ids.filtered(
                lambda o: o.status == "accepted"
            ):
                raise UserError("Only one offer can be accepted!")
            record.status = "accepted"
            record.property_id.write(
                {
                    "state": "offer_accepted",
                    "selling_price": record.price,
                    "buyer_id": record.partner_id.id,
                }
            )
        return True

    def action_refuse(self):
        for record in self:
            record.status = "refused"
        return True
