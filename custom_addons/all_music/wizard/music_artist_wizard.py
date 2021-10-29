from odoo import models, fields, api, _
import pprint as pp
import base64
import xml.dom.minidom


class MusicMenuWizard(models.TransientModel):
    _name = "music.menu.wizard"
    _description = "Menu wizard"

    xml_file = fields.Binary(string="Input xml")

    def download_file(self):
        xml_data = base64.b64decode(self.xml_file).decode("utf-8").strip()
        print(xml_data)
