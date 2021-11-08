from odoo import models, fields, api, _
from odoo.exceptions import UserError
import random


class MusicArtist(models.Model):
    """Model artist"""
    _name = "music.artist"
    _description = "Info about musician"

    color = fields.Integer(string='Color Index')
    name = fields.Char(string="Name", required=True)
    sex = fields.Selection([("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other")], string="Sex")
    age = fields.Char(string="Age")
    avatar = fields.Binary(string="Image")
    country_id = fields.Many2one("res.country", string="Country")
    month_listeners = fields.Integer(string="Month listeners")
    single_ids = fields.One2many(string="Singles", comodel_name="single", inverse_name="artist_id", required=True,
                                 ondelete="cascade")
    album_ids = fields.One2many(string="Albums", comodel_name="music.album", inverse_name="artist_id",
                                ondelete="cascade")
    group_id = fields.Many2one(string="Group", comodel_name="music.group")

    @api.onchange("name")
    def _onchange_name(self):
        """restriction on the introduction of an already created artist"""
        if self.env["music.artist"].search([("name", "=", self.name)]):
            raise UserError(_("Artist with the same name already exists"))

    @api.onchange("album_ids")
    def _onchange_album_ids(self):
        song_info = []
        for record in self.album_ids.single_ids:
            if record.name in self.single_ids.mapped("name"):
                raise UserError(_("Chose another name for song!"))
            else:
                context = {
                    "name": record.name,
                    "listeners": record.listeners,
                    "duration": record.duration,
                }
            song_info.append((0, 0, context))
        self.single_ids = song_info
