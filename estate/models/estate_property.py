from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Property of Estate"

    active = fields.Boolean(default=False)
    state = fields.Selection(
        selection=[('new', 'New'), 
        ('offer_received', 'Offer Received'), 
        ('offer_accepted', 'Offer Accepted'), 
        ('sold', 'Sold'), 
        ('canceled', 'Canceled')],
        default='new',required=True, copy=False
    )

    name = fields.Char(string="Title",
                        required=True)
    description = fields.Text()
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(
        string="Available From",
        default=lambda self: fields.Datetime.now() + relativedelta(months=3),
        copy=False
    )

    expected_price = fields.Float(string="Expected Price"
                                  , required=True)
    selling_price = fields.Float(string="Selling Price"
                                 , readonly=True
                                 , copy=False)

    bedrooms = fields.Integer(string="Bedrooms"
                              , default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), 
        ('south', 'South'), 
        ('east', 'East'), 
        ('west', 'West')]
    )