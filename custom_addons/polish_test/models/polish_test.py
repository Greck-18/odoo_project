from odoo import models, fields, api
from datetime import datetime


class PolishTest(models.Model):
    _name = "polish.test"
    _description = "Polish Test"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", translate=True, default="Dan")
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
    ])
    note = fields.Text(string="About yourself", help="Tell about yourself",
                       translate=True)
    date_of_birth = fields.Date(string="DateOFBirth")
    time = fields.Datetime(string="Time", help="Mould filling time", default=lambda *x: datetime.now())

    test_id = fields.Many2one(comodel_name="polish", string="Test")

    def wizard_open(self):
        wizard = {"type": "ir.actions.act_window",
                  "res_model": "polish.test.entry.wizard",
                  "view_mode": "form",
                  "target": "new"}
        return wizard


class Polish(models.Model):
    _name = "polish"
    _description = "Polish"

    polish_test_ids = fields.One2many(comodel_name="polish.test", inverse_name='test_id', string="polish")
