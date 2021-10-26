from odoo import models, fields, api
from datetime import datetime


class ResPartner(models.Model):
    _inherit = "res.partner"
    test = fields.Char(string="Test")
    is_wizard_made = fields.Boolean(string="Check")

    # def create(self, vals):
    #     result = super().create(vals)
    #     return result
