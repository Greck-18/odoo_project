from odoo import models, fields, api


class PolishTestEntry(models.TransientModel):
    _name = "polish.test.entry.wizard"
    _description = "Chose Test"

    test = fields.Selection([("english", "English"),
                             ("polish", "Polish"),
                             ("french", "French")], required=True)

    date = fields.Date(required=True, default=lambda self: fields.Date.context_today(self))

    def chose_test(self):
        print("Click")
        return True
