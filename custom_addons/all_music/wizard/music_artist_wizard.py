from odoo import models, fields, api, _
from odoo.exceptions import UserError
import base64
import datetime
import xml.etree.ElementTree as ET
import pprint


class MusicMenuWizard(models.TransientModel):
    _name = "music.menu.wizard"
    _description = "Menu wizard"

    xml_file = fields.Binary(string="Input xml")

    @staticmethod
    def convert_to_member(member):
        return {'name': member.text.strip()}

    # парсинг песен
    @staticmethod
    def singles(song_tag, artist_info):
        data = []
        for iter in song_tag.findall("songs/song"):
            artist_songs = {}
            for song in iter:
                if song.tag == "members":
                    song.text = list(map(MusicMenuWizard.convert_to_member, song.findall("member/name")))
                elif song.tag == "listeners":
                    song.text = int(song.text)
                artist_songs[song.tag] = song.text
            data.append((0, 0, artist_songs))
        artist_info[f"{song_tag.tag[:-1]}_ids"] = data

    # парсинг альбома
    @staticmethod
    def albums(albums_tag, artist_info):
        data = []
        artist_album = {}
        for iter in albums_tag.findall("album/songs/"):
            artist_album_songs = {}
            for album in iter:
                if album.tag == "members":
                    album.text = list(map(MusicMenuWizard.convert_to_member, album.findall("member/name")))[0]
                elif album.tag == "listeners":
                    album.text = int(album.text)
                artist_album_songs[album.tag] = album.text
            data.append((0, 0, artist_album_songs))
        for album in albums_tag.findall("album/"):
            if album.tag == "songs":
                artist_album["single_ids"] = data
            elif album.tag == "release_date":
                album.text = datetime.datetime.strptime(album.text.strip(), "%m-%d-%Y")
                artist_album[album.tag] = album.text
            else:
                artist_album[album.tag] = album.text.strip()
        artist_info[f"{albums_tag.tag[:-1]}_ids"] = [(0, 0, artist_album)]

    # информация об артистах
    def download_file(self):
        if not self.xml_file:
            raise UserError(_("Input your xml file!"))
        xml_data = base64.b64decode(self.xml_file).decode("utf-8").strip()
        myroot = ET.fromstring(xml_data)
        main_store = []
        for iter in myroot[0]:
            artist_info = {}
            for artist in iter:
                if artist.tag == "singles":
                    MusicMenuWizard.singles(artist, artist_info)
                elif artist.tag == "albums":
                    MusicMenuWizard.albums(artist, artist_info)
                else:
                    if artist.tag == "country":
                        artist.tag += "_id"
                    elif artist.tag == "month_listeners":
                        artist.text = int(artist.text)
                    artist_info[artist.tag] = artist.text
            main_store.append(artist_info)
        pprint.pprint(main_store)
        return self.env['music.artist'].create(main_store)
