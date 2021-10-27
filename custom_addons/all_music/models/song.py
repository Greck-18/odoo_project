from odoo import models, fields, api, _


class Song(models.Model):
    _name = "song"
    _description = "Info about song"
    name = fields.Char(string="Name", required=True, default=lambda self: self._default_name())
    listeners = fields.Integer(string="Listeners", required=True)
    duration = fields.Char(string="Duration", required=True)
    musician_id = fields.Many2one(string="Musician", comodel_name="musician", required=True)
    album_id = fields.Many2one(string="Album", comodel_name="music.album", required=True)
    group_id = fields.Many2one(string="Group", comodel_name="music.group", required=True)
