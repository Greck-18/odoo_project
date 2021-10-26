from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PolishTestEntry(models.TransientModel):
    _name = "polish.test.entry.wizard"
    _description = "Chose Test"

    name = fields.Char(string="Name")
    test = fields.Selection([("english", "English"),
                             ("polish", "Polish"),
                             ("french", "French")], required=True, string="Test")
    email = fields.Char(string="Email")

    is_wizard_made = fields.Boolean(string="Check")

    city = fields.Char(string="City")

    date = fields.Date(required=True, default=lambda self: fields.Date.context_today(self))

    def create_contact(self):
        context = {"display_name": self.name,
                   "email": self.email,
                   "city": self.city,
                   "date": self.date,
                   "test": self.test
                   }
        if not self.env["res.partner"].search([("name", "=", self.name)]):
            self.is_wizard_made = True
            return self.env["res.partner"].create(context)
        raise UserError(_("Chose another name"))
