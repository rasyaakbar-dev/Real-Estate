from dateutil.relativedelta import relativedelta

from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = "id desc"

    price = fields.Float(required=True)
    status = fields.Selection(
        selection=[("accepted", "Accepted"), ("refused", "Refused")],
        copy=False,
        required=True,
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(string="Validity", default=7)
    create_date = fields.Date(string="Creation Date", default=fields.Date.today())
    date_deadline = fields.Date(compute="_compute_date_deadline")

    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days=record.validity)

    @api.depends("", "")
    def _inverse_create_date(self):
        for record in self:
            record.create_date = record.date_deadline - relativedelta(days=record.validity)
