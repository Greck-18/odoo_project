from odoo import models, api, fields


class PolishTest2(models.Model):
    _name = "polish.test2"
    _description = "Polish Test2"

    text = fields.Text(string="Text")
    check1 = fields.Boolean(string="Test1")
    check2 = fields.Boolean(string="Test2")
    check_all = fields.Boolean(string="Select all")
    select1 = fields.Selection(
        [("1", "1"),
         ("2", "2"),
         ("3", "3")
         ])
    select2 = fields.Selection([
        ("4", "4"),
        ("5", "5"),
        ("6", "6")
    ])
    boolean1 = fields.Boolean(string="1")
    boolean2 = fields.Boolean(string="2")
    boolean3 = fields.Boolean(string="3")
    boolean4 = fields.Boolean(string="4")
    boolean5 = fields.Boolean(string="5")
    boolean6 = fields.Boolean(string="6")
    boolean7 = fields.Boolean(string="7")
    boolean8 = fields.Boolean(string="8")
    boolean9 = fields.Boolean(string="9")

    @api.onchange("check_all")
    def _onchange_check_all(self):
        if self.check_all:
            self.check1 = self.check2 = True
            self.text = "{%s}" % (self.env["polish.test2"]._fields['check2'].string)
        else:
            self.check1 = self.check2 = False
            self.text = ""

    @api.onchange("check1")
    def _onchange_check1(self):
        if self.check1 and not self.check2:
            self.text = f"[{self.env['polish.test2']._fields['check1'].string}]"
        elif self.check1 and self.check2:
            self.text = "{%s}" % (self.env["polish.test2"]._fields[
                                      'check2'].string) + f" [{self.env['polish.test2']._fields['check1'].string}]"
        elif not self.check1 and self.check2:
            self.text = self.text.split()[0]
        elif not self.check2 and not self.check1:
            self.text = ""

    @api.onchange("check2")
    def _onchange_check2(self):
        if self.check2 and not self.check1:
            self.text = "{%s}" % (self.env["polish.test2"]._fields['check2'].string)
        elif self.check2 and self.check1:
            self.text = f"[{self.env['polish.test2']._fields['check1'].string}]" + " {%s}" % (
                self.env["polish.test2"]._fields['check2'].string)
        elif not self.check2 and self.check1:
            self.text = self.text.split()[0]
        elif not self.check2 and not self.check1:
            self.text = ""
