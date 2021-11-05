from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MusicGroup(models.Model):
    _name = "music.group"
    _description = "Info about group"
    name = fields.Char(string="Name", required=True)
    avatar = fields.Binary(string="Image")
    month_listeners = fields.Integer(string="Month listeners", required=True)
    artist_ids = fields.One2many(string="Artist", comodel_name="music.artist", inverse_name="group_id",
                                 required=True, ondelete="cascade")
    album_ids = fields.One2many(string="Album", comodel_name="music.album", inverse_name="group_id", ondelete="cascade")
    single_ids = fields.One2many(string="Song", comodel_name="single", inverse_name="group_id", required=True,
                                 ondelete="cascade")


    @api.onchange("name")
    def _onchange_name(self):
        if self.env["music.group"].search([("name", "=", self.name)]):
            raise UserError(_("A group with the same name already exists"))
