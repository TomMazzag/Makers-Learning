import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repo import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

@app.route('/albums', methods = ['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    #print(repo.all())
    return "\n".join(
        f"{album}" for album in repo.all()
    )

@app.route('/albums', methods = ['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    album = request.form
    repo.create(Album(None, 
                      album['title'],
                      album['release_year'],
                      album['artist_id']))
    return ""

@app.route('/artists', methods = ['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    return "\n".join(
        f"{artist}" for artist in repo.all()
    )

@app.route('/artists', methods = ['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artist = request.form
    repo.create(Artist(None,
                       artist['name'],
                       artist['genre']))
    return '', 200


from example_routes import apply_example_routes
apply_example_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

