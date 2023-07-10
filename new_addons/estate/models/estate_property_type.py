from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "A model representing types of real estate objects"

    name = fields.Char(required=True)
