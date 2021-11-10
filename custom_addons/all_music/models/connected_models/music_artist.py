from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MusicArtist(models.Model):
    """Model artist"""
    _name = "music.artist"
    _description = "Info about musician"

    name = fields.Char(string="Name", required=True)
    sex = fields.Selection([("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other")], string="Sex")
    single_listeners = fields.Integer(string="Single listeners", store=True)
    age = fields.Integer(string="Age")
    avatar = fields.Image(string="Image")
    country_id = fields.Many2one(comodel_name="res.country", string="Country")
    month_listeners = fields.Integer(string="Month listeners")
    single_ids = fields.One2many(comodel_name="single", inverse_name="artist_id", string="Singles", required=True,
                                 ondelete="cascade")
    album_ids = fields.One2many(comodel_name="music.album", inverse_name="artist_id", string="Albums",
                                ondelete="cascade")
    group_id = fields.Many2one(comodel_name="music.group", string="Group")

    @api.onchange("name")
    def _onchange_name(self):
        if self.env["music.artist"].search([("name", "=", self.name)]):
            raise UserError(_("Group with the same name already exists"))

    @api.onchange("album_ids")
    def _onchange_album_ids(self):
        song_info = []
        for record in self.album_ids.single_ids:
            if record.name in self.single_ids.mapped("name"):
                raise UserError(_("Chose another name for song!"))
            else:
                context = {
                    "name": record.name,
                    "listeners": record.listeners,
                    "duration": record.duration,
                }
            song_info.append((0, 0, context))
        self.single_ids = song_info

    # @api.depends("single_ids.listeners")
    # def _compute_total(self):
    #     for record in self:
    #         record.single_listeners = sum(record.single_ids.mapped("listeners"))

    def wizard(self):
        wizard = {"type": "ir.actions.act_window",
                  "res_model": "music.artist.tree.wizard",
                  "view_mode": "form",
                  "target": "new",
                  "context": {"default_name": self.name,
                              "default_single_ids": self.single_ids.ids,
                              "default_month_listeners": self.month_listeners,
                              "default_single_listeners": self.single_listeners}
                  }

        return wizard
