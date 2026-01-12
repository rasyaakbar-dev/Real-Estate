from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "id desc"

    # Main identifier field
    name = fields.Char(required=True)
