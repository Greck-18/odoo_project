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

    def convert_to_country_code(self, artist, artist_info):
        """convert countries to codes"""
        if artist.text == "Australia":
            country_code = "AU"
        elif artist.text == "UK":
            country_code = "GB"
        else:
            country_code = "US"
        artist_info[f"{artist.tag}_id"] = self.env['res.country'].search([('code', '=', country_code)]).id

    def parse_song_album_info(self, song):
        """parsing the main info in songs and albums"""
        if song.tag == "members":
            song.text = self._convert_to_member(song)
        elif song.tag == "listeners":
            song.text = int(song.text)
        elif song.tag == "duration":
            song.text = float(song.text.replace(':', '.'))

    def create_artist_record(self, artist_store, group_store):
        """Create record if not exists , if exists only update record"""
        for artist in artist_store:
            if self.env['music.artist'].search([('name', '=', artist['name'])]):
                self.env['music.artist'].update(artist)
            else:
                self.env['music.artist'].create(artist)
        for group in group_store:
            if self.env['music.group'].search([('name', '=', group['name'])]):
                self.env['music.group'].update(group)
            else:
                self.env['music.group'].create(group)

    def group_artist_listeners(self, group_store):
        """Add listeners for each group artist"""
        for i, w in enumerate(group_store):
            for record in self.env["music.artist"].search([("group_id", '=', group_store[i]['name'])]):
                record.month_listeners = self.env['music.group'].search(
                    [("name", "=", group_store[i]['name'])]).month_listeners

    @staticmethod
    def _convert_to_member(member_tag):
        """The function parses all members in the song"""
        member = ""
        for i in member_tag.findall("member/name"):
            member += f"{i.text.strip()},"
        return member[:-1]

    def _parse_singles(self, song_tag, artist_info):
        """The function parses all information about the songs of the artist and the group"""
        data = []
        for songs in song_tag.findall("songs/song"):
            artist_songs = {}
            for song in songs:
                self.parse_song_album_info(song)
                artist_songs[song.tag] = song.text
            data.append((0, 0, artist_songs))
        artist_info[f"{song_tag.tag[:-1]}_ids"] = data

    def _parse_albums(self, albums_tag, artist_info):
        """The function parses all information about the artist's and group's album"""
        data = []
        artist_album = {}
        for albums in albums_tag.findall("album/songs/"):
            artist_album_songs = {}
            for album in albums:
                self.parse_song_album_info(album)
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

    def _parse_group_artists(self, group_tag, group_info):
        """The function parses all information about the artist of the group"""
        data = []
        for group in group_tag.findall("artist"):
            group_artists = {}
            for artist in group:
                if artist.tag == "country":
                    self.convert_to_country_code(artist, group_artists)
                else:
                    if artist.tag == "age":
                        artist.text = int(artist.text)
                    group_artists[artist.tag] = artist.text
            data.append((0, 0, group_artists))
        group_info[f"{group_tag.tag[:-1]}_ids"] = data

    def download_file(self):
        """ The function takes xml file and parses it"""
        artist_store = []
        group_store = []
        if not self.xml_file:
            raise UserError(_("Input your xml file!"))
        xml_data = base64.b64decode(self.xml_file).decode("utf-8").strip()
        my_root = ET.fromstring(xml_data)
        for artists in my_root.find("./Artists"):
            artist_info = {}
            for artist in artists:
                if artist.tag == "singles":
                    self._parse_singles(artist, artist_info)
                elif artist.tag == "albums":
                    self._parse_albums(artist, artist_info)
                else:
                    if artist.tag == "country":
                        self.convert_to_country_code(artist, artist_info)
                    elif artist.tag in ("month_listeners", "age"):
                        artist_info[artist.tag] = int(artist.text)
                    else:
                        artist_info[artist.tag] = artist.text
            artist_store.append(artist_info)

        for groups in my_root.find("./Groups"):
            group_info = {}
            for group in groups:
                if group.tag == "singles":
                    self._parse_singles(group, group_info)
                elif group.tag == "albums":
                    self._parse_albums(group, group_info)
                elif group.tag == "artists":
                    self._parse_group_artists(group, group_info)
                else:
                    if group.tag == "month_listeners":
                        group_info[group.tag] = int(group.text)
                    else:
                        group_info[group.tag] = group.text.strip()
            group_store.append(group_info)

        self.create_artist_record(artist_store, group_store)
        self.group_artist_listeners(group_store)
