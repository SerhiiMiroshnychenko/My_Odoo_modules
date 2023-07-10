from odoo import api, fields, models

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
    garden = fields.Boolean()
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
    property_type_id = fields.Many2one("estate.property.type", string="Type")
    salesperson_id = fields.Many2one(
        'res.users',
        string='Salesperson',
        default=lambda self: self.env.user)
    buyer_id = fields.Many2one(
        "res.partner",
        string="Buyer",
        copy=False,
    )
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id")

    total_area = fields.Float(compute="_compute_total_area")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for estate in self:
            print(estate.title)  # TODO Убрати після налагодження
            print(estate.best_price)  # TODO Убрати після налагодження
            estate.total_area = estate.living_area + estate.garden_area


    best_price = fields.Float(compute="_compute_best_price")

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for estate in self:
            estate.best_price = max(estate.offer_ids.mapped('price'))\
                if estate.offer_ids else 0
