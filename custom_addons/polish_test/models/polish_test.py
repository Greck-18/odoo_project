from odoo import models, fields, api
from datetime import datetime


class PolishTest(models.Model):
    _name = "polish.test"
    _description = "Polish Test"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    respondent_name = fields.Char(string="Name")

    name = fields.Char(string="Name", translate=True)
    age = fields.Integer(string="Age", default="18")
    is_work = fields.Boolean(string="Work", help="Click,if you work")
    email = fields.Char(string="email", size=50)
    height = fields.Float(string="Height", digits=(4, 1))
    photo = fields.Binary(string="Photo", help="Upload file")
    message = fields.Html(string="Message")
    image = fields.Image(string="Image")
    currency_id = fields.Many2one("res.currency", string="currency")
    salary = fields.Monetary(string="Salary")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")
    note = fields.Text(string="About yourself", help="Tell about yourself",
                       translate=True)
    date_of_birth = fields.Date(string="DateOFBirth")
    time = fields.Datetime(string="Time", help="Mould filling time", default=lambda *x: datetime.now())

    test_id = fields.Many2one(comodel_name="polish", string="Test")

    partner_id = fields.Many2one("res.partner", string="Partner", on_delete="set null",
                                 )

    # partner_city = fields.Char(string="Partner city", related="partner_id.city", readonly=True)

    def wizard_open(self):
        wizard = {"type": "ir.actions.act_window",
                  "res_model": "polish.test.entry.wizard",
                  "view_mode": "form",
                  "target": "new",
                  "context": {"default_name": self.name,
                              # "default_city": self.partner_city,
                              "default_email": self.email}}
        return wizard
