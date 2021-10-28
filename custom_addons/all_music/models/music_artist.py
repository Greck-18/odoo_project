from odoo import models, fields, api, _


class MusicArtist(models.Model):
    _name = "music.artist"
    _description = "Info about musician"

    name = fields.Char(string="Name")
    sex = fields.Selection([("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other")], string="Sex")
    age = fields.Integer(string="Age")
    avatar = fields.Binary(string="Image")
    country = fields.Char(string="Country")
    month_listeners = fields.Integer(string="Month listeners")
    song_ids = fields.One2many(string="Song", comodel_name="song", inverse_name="musician_id",required=True)
    album_ids = fields.One2many(string="Album", comodel_name="music.album", inverse_name="musician_id")
    group_id = fields.Many2one(string="Group", comodel_name="music.group")

    def wizard_open(self):
        print("Nice")
