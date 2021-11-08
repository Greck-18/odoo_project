from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MusicAlbum(models.Model):
    """Model album"""
    _name = "music.album"
    _description = "Musician album"

    name = fields.Char(string="Name", required=True)
    release_date = fields.Date(string="Date of release")
    artist_id = fields.Many2one(string="Artist", comodel_name="music.artist")
    # TODO:need check this ondelete parameter
    single_ids = fields.One2many(string="Song", comodel_name="single", inverse_name="album_id", required=True,
                                 ondelete="cascade")
    group_id = fields.Many2one(string="Group", comodel_name="music.group")

    @api.onchange("name")
    def _onchange_name(self):
        if self.env["music.album"].search([("name", "=", self.name)]):
            raise UserError(_("Group with the same name already exists"))
