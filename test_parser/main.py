import xml.etree.ElementTree as ET
import pprint
import re

mytree = ET.parse("api_music.xml")
myroot = mytree.getroot()


main_store = []
artist_album = {}



def convertToText(object):
    return {'name': object.text.strip()}


def singles(song_tag, artist_info):
    data = []
    for i in song_tag.findall("songs/song"):
        artist_songs = {}
        for j in i:
            if j.tag == "members":
                j.text = list(map(convertToText, j.findall("member/name")))
            artist_songs[j.tag] = j.text
        data.append(artist_songs)
    artist_info[song_tag.tag] = data


def albums(albums_tag, artist_info):
    data = []
    for i in albums_tag.findall("album/songs/"):
        artist_album_info = {}
        for j in i:
            if j.tag == "members":
                j.text = list(map(convertToText, j.findall("member/name")))[0]
            artist_album_info[j.tag] = j.text
        data.append(artist_album_info)
    for z in albums_tag.findall("album/"):
        if z.tag == "songs":
            artist_album[z.tag] = data
        else:
            artist_album[z.tag] = z.text.strip()
    print()
    #data.append(artist_album)
    #artist_info[albums_tag.tag] = data

    # print(data)


# информация об артистах
for iter in myroot[0]:
    artist_info = {}
    name = iter.find('name').text
    for j in iter:
        if j.tag == "singles":
            singles(j, artist_info)
        elif j.tag == "albums":
            albums(j, artist_info)
        else:
            artist_info[j.tag] = j.text.strip()
    main_store.append(artist_info)

pprint.pprint(main_store)
