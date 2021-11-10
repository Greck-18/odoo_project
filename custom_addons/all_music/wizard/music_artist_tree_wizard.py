from odoo import fields, models, api


class MusicArtistTreeWizard(models.TransientModel):
    _name = "music.artist.tree.wizard"
    _description = "Wizard on tree view"

    name = fields.Char(string="Name")
    single_ids = fields.One2many(string="Singles", comodel_name="single", inverse_name="artist_id", required=True,
                                 ondelete="cascade")
    month_listeners = fields.Integer(string="Month listeners")

    single_listeners = fields.Integer(string="Single listeners")



    def update(self, vals):
        context = {"month_listeners": self.month_listeners,
                   "single_listeners": self.single_listeners,
                   "name": self.name,
                   "single_ids": self.single_ids.ids
                   }

        return self.env["music.artist"].update(context)
