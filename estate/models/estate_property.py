from dateutil.relativedelta import relativedelta

from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Properties of Real Estate"
    _order = "id desc"

    # Main identifier field
    name = fields.Char(string="Title", required=True)

    # Technical/special fields
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled'),
        ],
        string="Status",
        default='new',
        required=True,
        copy=False,
    )

    # Simple fields
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ],
        string="Garden Orientation",
    )

    # Relational fields
    property_type_id = fields.Many2one("estate.property.type", string="Property Type", required=True)
    buyer = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)

    # Numeric fields
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)

    # Date fields
    date_availability = fields.Date(
        string="Available From",
        default=lambda self: fields.Date.today() + relativedelta(months=3),
        copy=False,
    )