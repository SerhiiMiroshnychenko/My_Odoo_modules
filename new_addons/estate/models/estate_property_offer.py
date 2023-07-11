from odoo import api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "A model representing offers for real estate objects"

    price = models.fields.Float()
    status = fields.Selection(
        copy=False,
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        help="The status of offer for real estate object"
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Partner",
        required=True,
    )
    property_id = fields.Many2one(
        "estate.property",
        required=True,
    )

    validity = fields.Integer(default=7, string='Validity (days)')

    date_deadline = fields.Date(
        compute='_compute_date_deadline',
        inverse='_inverse_date_deadline',
        string='Deadline'
    )

    @api.depends('validity')
    def _compute_date_deadline(self):
        for offer in self:
            create_date = offer.create_date or date.today()
            offer.date_deadline = create_date + relativedelta(
                days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            create_date = offer.create_date or date.today()
            date_difference = offer.date_deadline - create_date.date()
            offer.validity = date_difference.days
            print(f'Create date: {create_date}\n'
                  f'Date deadline: {offer.date_deadline}\n'
                  f'Date difference: {date_difference}\n'
                  f'Validity (days): {offer.validity}')


