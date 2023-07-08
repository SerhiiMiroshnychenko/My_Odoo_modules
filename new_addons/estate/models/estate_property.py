from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "A model representing real estate objects"

    title = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,
                                    default=lambda self: fields.Datetime.add(
        value=fields.Datetime.today(),
        months=3
    ))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="The side of the world on which the garden is oriented")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        required=True,
        copy=False,
        string='State',
        selection=[
            ('new', 'New'),
            ('offer received', 'Offer Received'),
            ('offer accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled'),
        ],
        default='new',
        help="The state of the real estate object"
    )


