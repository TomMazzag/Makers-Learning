from lib.artist import Artist

# id, name, genre

def test_artist():
    artist = Artist(1, "Taylor Swift", "Pop")
    assert artist.id == 1
    assert artist.name == 'Taylor Swift'
    assert artist.genre == 'Pop'


def test_equal():
    artist1 = Artist(1, "Taylor Swift", "Pop")
    artist2 = Artist(1, "Taylor Swift", "Pop")
    assert artist2 == artist1

def test_format():
    #"Artist {self.id}: {self.name}, {self.genre}"
    artist1 = Artist(1, "Taylor Swift", "Pop")
    assert str(artist1) == "Artist 1: Taylor Swift, Pop"