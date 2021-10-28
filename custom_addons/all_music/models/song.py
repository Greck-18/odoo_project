from odoo import models, fields, api, _


class Song(models.Model):

    _name = "song"
    _description = "Info about song"
    name = fields.Char(string="Name", required=True)
    listeners = fields.Integer(string="Listeners", required=True)
    duration = fields.Char(string="Duration", required=True)
    musician_id = fields.Many2one(string="Musician", comodel_name="music.artist")
    album_id = fields.Many2one(string="Album", comodel_name="music.album")
    group_id = fields.Many2one(string="Group", comodel_name="music.group")
