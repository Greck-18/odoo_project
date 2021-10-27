from odoo import models, fields, api, _


class Group(models.Model):
    _name = "musical.group"
    _description = "Info about group"
    name = fields.Char(string="Name", required=True)
    month_listeners = fields.Integer(string="Month listeners", required=True)
    musician_ids = fields.One2many(string="Musician", comodel_name="musician", inverse_name="group_id")
    album_ids = fields.One2many(string="Album", comodel_name="music.album", inverse_name="group_id")
    song_ids = fields.One2many(string="Song", comodel_name="song", inverse_name="group_id")
