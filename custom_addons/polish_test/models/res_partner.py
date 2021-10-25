from odoo import models, fields, api
from datetime import datetime


class ResPartner(models.Model):
    _inherit = "res.partner"

    registration_date = fields.Datetime(string="Time", help="Mould filling time", default=lambda *x: datetime.now())
