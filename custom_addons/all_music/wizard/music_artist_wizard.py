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

    # парсинг песен
    @staticmethod
    def _parse_singles(song_tag, artist_info):
        data = []
        for iter in song_tag.findall("songs/song"):
            artist_songs = {}
            for song in iter:
                if song.tag == "members":
                    song.tag = f"{song.tag[:-1]}_ids"
                    song.text = "member"
                    # MusicMenuWizard._pars_id_member()
                    # MusicMenuWizard._convert_to_member(song.findall('member/name'))
                    # song.text=
                elif song.tag == "listeners":
                    song.text = int(song.text)
                artist_songs[song.tag] = song.text
            data.append((0, 0, artist_songs))
        artist_info[f"{song_tag.tag[:-1]}_ids"] = data

    # парсинг альбома
    @staticmethod
    def _parse_albums(albums_tag, artist_info):
        data = []
        artist_album = {}
        for iter in albums_tag.findall("album/songs/"):
            artist_album_songs = {}
            for album in iter:
                if album.tag == "members":
                    album.tag = f"{album.tag[:-1]}_ids"
                    album.text = "member"
                    # MusicMenuWizard._convert_to_member(album)
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

    # @staticmethod
    def _parse_group_artists(self, group_tag, group_info):
        data = []
        for iter in group_tag.findall("artist"):
            group_artists = {}
            for artist in iter:
                if artist.tag == "country":
                    if artist.text == "Australia":
                        country_code = "AU"
                    elif artist.text == "UK":
                        country_code = "GB"
                    else:
                        country_code = "US"
                    artist.text = artist.text = self.env['res.country'].search([('code', '=', country_code)]).id
                    artist.tag += "_id"
                group_artists[artist.tag] = artist.text
            data.append((0, 0, group_artists))
        group_info[f"{group_tag.tag[:-1]}_ids"] = data

    # информация об артистах
    def download_file(self):
        print(self.env['music.artist'].name)
        artist_store = []
        group_store = []
        if not self.xml_file:
            raise UserError(_("Input your xml file!"))
        xml_data = base64.b64decode(self.xml_file).decode("utf-8").strip()
        myroot = ET.fromstring(xml_data)
        for iter in myroot[0]:
            artist_info = {}
            for artist in iter:
                if artist.tag == "singles":
                    MusicMenuWizard._parse_singles(artist, artist_info)
                elif artist.tag == "albums":
                    MusicMenuWizard._parse_albums(artist, artist_info)
                else:
                    if artist.tag == "country":
                        if artist.text == "Australia":
                            country_code = "AU"
                        elif artist.text == "UK":
                            country_code = "GB"
                        else:
                            country_code = "US"
                        artist.text = artist.text = self.env['res.country'].search([('code', '=', country_code)]).id
                        artist.tag += "_id"
                    elif artist.tag == "month_listeners":
                        artist.text = int(artist.text)
                    artist_info[artist.tag] = artist.text
            artist_store.append(artist_info)

        for iter in myroot[1]:
            group_info = {}
            for group in iter:
                if group.tag == "singles":
                    MusicMenuWizard._parse_singles(group, group_info)
                elif group.tag == "albums":
                    MusicMenuWizard._parse_albums(group, group_info)
                elif group.tag == "artists":
                    MusicMenuWizard._parse_group_artists(self, group, group_info)
                else:
                    if group.tag == "month_listeners":
                        group_info[group.tag] = int(group.text)
                    else:
                        group_info[group.tag] = group.text.strip()
            group_store.append(group_info)

        pprint.pprint(artist_store)
        self.env["music.artist"].create(artist_store)
        self.env["music.group"].create(group_store)
