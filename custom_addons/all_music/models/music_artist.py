from odoo import models, fields, api, _
from odoo.exceptions import UserError
import random


class MusicArtist(models.Model):
    _name = "music.artist"
    _description = "Info about musician"

    # def _get_default_color(self):
    #     return random.randint(1, 11)

    color = fields.Integer(string='Color Index')
    name = fields.Char(string="Name")
    sex = fields.Selection([("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other")], string="Sex")
    age = fields.Char(string="Age")
    avatar = fields.Binary(string="Image")
    country_id = fields.Many2one('res.country', string='Country')
    # country_id = fields.Char(string="Country")  #
    # state_ids = fields.Many2many('res.country.state', string='Federal States')
    month_listeners = fields.Integer(string="Month listeners")
    single_ids = fields.One2many(string="Singles", comodel_name="single", inverse_name="artist_id", required=True)
    album_ids = fields.One2many(string="Albums", comodel_name="music.album", inverse_name="musician_id")
    group_id = fields.Many2one(string="Group", comodel_name="music.group")

    @api.onchange("album_ids")
    def _onchange_album_ids(self):
        for iter in self:
            song_info = []
            for rec in self.album_ids.single_ids:
                if rec.name in iter.single_ids.mapped("name"):
                    raise UserError(_("Chose another name for song!"))
                else:
                    context = {
                        "name": rec.name,
                        "listeners": rec.listeners,
                        "duration": rec.duration,
                    }
                song_info.append((0, 0, context))
            iter.single_ids = song_info

    # @api.onchange("name")
    # def _onchange_name(self):
    #     if self.env["music.artist"].search([("name", "=", self.name)]):
    #         raise UserError(_("Chose another name for artist!"))
