from odoo import models, fields, api, _


class Musician(models.Model):
    _name = "musician"
    _description = "Info about musician"

    name = fields.Char(string="Name", required=True, default=lambda self: self._default_name())
    sex = fields.Selection([("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other")], string="Sex")
    country = fields.Char(string="Country", required=True, translate=True)
    month_listeners = fields.Integer(string="Month listeners", required=True)
    song_ids = fields.One2many(string="Song", comodel_name="song", inverse_name="musician_id", required=True)
    album_ids = fields.One2many(string="Album", comodel_name="music.album", inverse_name="musician_id", required=True)
    group_id = fields.Many2one(string="Group", comodel_name="music.group", required=True)

