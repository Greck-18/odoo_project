from odoo import models, fields, api, _


class MusicGroup(models.Model):
    _name = "music.group"
    _description = "Info about group"
    name = fields.Char(string="Name", required=True)
    avatar = fields.Binary(string="Image")
    month_listeners = fields.Integer(string="Month listeners", required=True)
    musician_ids = fields.One2many(string="Musician", comodel_name="music.artist", inverse_name="group_id",
                                   required=True)
    album_ids = fields.One2many(string="Album", comodel_name="music.album", inverse_name="group_id")
    single_ids = fields.One2many(string="Song", comodel_name="single", inverse_name="group_id", required=True)

    def wizard_open(self):
        print("hello")
