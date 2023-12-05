from lib.artist_repo import ArtistRepository
from lib.artist import Artist

def test_artist_repository_all(db_connection):
    db_connection.seed('seeds/artist_table.sql')
    repository = ArtistRepository(db_connection)
    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]