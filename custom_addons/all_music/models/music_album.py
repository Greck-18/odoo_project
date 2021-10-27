from odoo import models, fields, api, _


class Album(models.Model):
    _name = "music.album"
    _description = "Musician album"

    name = fields.Char(string="Name", required=True)
    release_data = fields.Date(string="Date of release")
    musician_id = fields.Many2one(string="Musician", comodel_name="musician", required=True)
    song_ids = fields.One2many(string="Song", comodel_name="song", inverse_name="album_id", required=True)
    group_id = fields.Many2one(string="Group", comodel_name="music.group", required=True)
