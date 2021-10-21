from odoo import models, fields, api
from datetime import datetime


class PolishTest(models.Model):
    _name = "polish.test"
    _description = "Polish Test"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True, translate=True, default="Dan")
    age = fields.Integer(string="Age", required=True, default="18")
    is_work = fields.Boolean(string="Work", help="Click,if you work", required=True)
    email = fields.Char(string="email", required=True, size=50)
    height = fields.Float(string="Height", digits=(4, 1))
    photo = fields.Binary(string="Photo", help="Upload file")
    message = fields.Html(string="Message")
    image = fields.Image(string="Image")
    currency_id = fields.Many2one("res.currency", string="currency")
    salary = fields.Monetary(string="Salary", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    note = fields.Text(string="About yourself", help="Tell about yourself", required=True,
                       translate=True)
    date_of_birth = fields.Date(string="DateOFBirth", required=True)
    time = fields.Datetime(string="Time", help="Mould filling time", default=lambda *x: datetime.now())
