from lib.artist import Artist

class ArtistRepository():

    def __init__(self, connection):
        self.connection =  connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM artists")
        artists = []
        for row in rows:
            artist = Artist(row['id'], row['name'], row['genre'])
            artists.append(artist)
        return (artists)
    
    def create(self, artist):
        #INSERT INTO artists (name, genre) VALUES ('Pixies', 'Rock');
        rows = self.connection.execute("INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id", [artist.name, artist.genre])
        row = rows[0]
        artist.id = row["id"]
        return None