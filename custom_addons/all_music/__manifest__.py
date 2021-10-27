{
    'name': 'AllMusic',
    'version': '1.1',
    'summary': '',
    'sequence': 1,
    'description': "Information about musicians",
    'category': '',
    'website': '',
    'images': [
    ],
    'depends': ['base'],
    'data': [
        'views/music_album_views.xml',
        'views/music_group_views.xml',
        'views/musician_views.xml',
        'views/song_views.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
