import xml.etree.ElementTree as ET
import pprint
import re


#
#
def convert_to_member(member):
    return {'name': member.text.strip()}


# парсинг песен
def singles(song_tag, artist_info):
    data = []
    for iter in song_tag.findall("songs/song"):
        artist_songs = {}
        for song in iter:
            if song.tag == "members":
                song.text = list(map(convert_to_member, song.findall("member/name")))
            artist_songs[song.tag] = song.text
        data.append(artist_songs)
    artist_info[song_tag.tag] = [0, 0, data]


# парсинг альбома
def albums(albums_tag, artist_info):
    data = []
    artist_album = {}
    for iter in albums_tag.findall("album/songs/"):
        artist_album_songs = {}
        for album in iter:
            if album.tag == "members":
                album.text = list(map(convert_to_member, album.findall("member/name")))[0]
            artist_album_songs[album.tag] = album.text
        data.append(artist_album_songs)
    for album in albums_tag.findall("album/"):
        if album.tag == "songs":
            artist_album[album.tag] = data
        else:
            artist_album[album.tag] = album.text.strip()
    artist_info[albums_tag.tag] = [0, 0, artist_album]


#
#
# # информация об артистах
# def main():
#     mytree = ET.parse("api_music.xml")
#     myroot = mytree.getroot()
#     main_store = []
#     for iter in myroot[0]:
#         artist_info = {}
#         for artist in iter:
#             if artist.tag == "singles":
#                 singles(artist, artist_info)
#             elif artist.tag == "albums":
#                 albums(artist, artist_info)
#             else:
#                 artist_info[artist.tag] = artist.text.strip()
#         main_store.append(artist_info)
#     return main_store
#
#
# main()


def main():
    group_store = []
    mytree = ET.parse("api_music.xml")
    myroot = mytree.getroot()
    main_store = []
    for iter in myroot:
        artist_info = {}
        for artist in iter.findall('artist/'):
            if artist.tag == "singles":
                singles(artist, artist_info)
            elif artist.tag == "albums":
                albums(artist, artist_info)
            else:
                artist_info[artist.tag] = artist.text.strip()
        main_store.append(artist_info)
    return main_store

    # for iter in myroot[1]:
    #     group_info = {}
    #     for group in iter:
    #         if group.tag == "singles":
    #             singles(group, group_info)
    #         elif group.tag == "albums":
    #             albums(group, group_info)
    #         elif group.tag == "artists":
    #             parse_group_artists(group, group_info)
    #         else:
    #             group_info[group.tag] = group.text.strip()
    #     group_store.append(group_info)
    # print(group_store)


pprint.pprint(main())
