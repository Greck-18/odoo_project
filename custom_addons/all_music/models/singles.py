from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Single(models.Model):
    """Model song"""
    _name = "single"
    _description = "Info about song"
    name = fields.Char(string="Name", required=True)
    listeners = fields.Integer(string="Listeners", required=True)
    duration = fields.Float(string="Duration", required=True)
    members = fields.Char(string="Members")
    artist_id = fields.Many2one(string="Artist", comodel_name="music.artist")
    album_id = fields.Many2one(string="Album", comodel_name="music.album")
    group_id = fields.Many2one(string="Group", comodel_name="music.group")

    @api.onchange("name")
    def _onchange_name(self):
        """restriction on the introduction of an already created song"""
        if self.env["single"].search([("name", "=", self.name)]):
            raise UserError(_("A song with the same name already exists"))
