from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "name"

    _sql_constraints = [
        ("unique_type_name", "UNIQUE(name)", "The type name must be unique"),
    ]

    name = fields.Char(string="Type Name", required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")