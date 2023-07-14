from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "A model representing types of real estate objects"
    _order = "sequence, name"

    name = fields.Char(required=True)
    sequence = fields.Integer(
        'Sequence',
        default=1,
        help="Used to order stages. Lower is better."
    )

    property_ids = fields.One2many('estate.property', 'property_type_id')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Type name already exists !"),
    ]
