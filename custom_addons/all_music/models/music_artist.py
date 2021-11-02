from odoo import models, fields, api, _


class MusicArtist(models.Model):
    _name = "music.artist"
    _description = "Info about musician"

    name = fields.Char(string="Name")
    sex = fields.Selection([("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other")], string="Sex")
    age = fields.Char(string="Age")
    avatar = fields.Binary(string="Image")
    # fields.Many2one("res.country", string="Country")
    country_id = fields.Char(string="Country")
    month_listeners = fields.Integer(string="Month listeners")
    single_ids = fields.One2many(string="Singles", comodel_name="single", inverse_name="artist_id", required=True)
    album_ids = fields.One2many(string="Albums", comodel_name="music.album", inverse_name="musician_id")
    group_id = fields.Many2one(string="Group", comodel_name="music.group")
