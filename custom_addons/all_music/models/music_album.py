from odoo import models, fields, api, _


class MusicAlbum(models.Model):
    _name = "music.album"
    _description = "Musician album"

    name = fields.Char(string="Name", required=True)
    release_date = fields.Date(string="Date of release")
    musician_id = fields.Many2one(string="Musician", comodel_name="music.artist")
    single_ids = fields.One2many(string="Song", comodel_name="single", inverse_name="album_id", required=True)
    group_id = fields.Many2one(string="Group", comodel_name="music.group")
