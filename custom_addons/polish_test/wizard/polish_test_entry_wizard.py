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

    is_polish_test_wizard_made = fields.Boolean(string="Check")

    city = fields.Char(string="City")

    date = fields.Date(string="Date", required=True, default=lambda self: fields.Date.context_today(self))

    def create_contact(self):
        if not self.env["res.partner"].search([("name", "=", self.name)]):
            self.is_polish_test_wizard_made = True
            context = {"display_name": self.name,
                       "email": self.email,
                       "city": self.city,
                       "date": self.date,
                       "test": self.test,
                       "is_polish_test_wizard_made": self.is_polish_test_wizard_made
                       }

            return self.env["res.partner"].create(context)
        raise UserError(_("Chose another name"))
