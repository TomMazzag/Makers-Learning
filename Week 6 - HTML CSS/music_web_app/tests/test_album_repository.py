from lib.album_repository import *
from lib.album import Album

"""
When all is called
All albums are returned as instances
"""

def test_all(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
    ]

