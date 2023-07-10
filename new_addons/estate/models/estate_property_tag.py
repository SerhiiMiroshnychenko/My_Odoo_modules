from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "A model representing tags of real estate objects"

    name = fields.Char(required=True)
