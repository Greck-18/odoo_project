from odoo import models, fields, api, _


class MusicArtistEntry(models.TransientModel):
    _name = "music.album.entry.wizard"
    _description = "Input xml file"

    xml_file = fields.Binary(string="Xml file", required=True)


    def download_file(self):
        pass
