from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _order = "id desc"

    # Main identifier field
    name = fields.Char(required=True)
