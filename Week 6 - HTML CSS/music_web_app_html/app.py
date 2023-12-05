import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repo import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    all_albums = repo.all()
    return render_template("albums.html", albums = all_albums)

@app.route('/albums/<id>')
def get_single_album(id):
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    all_albums = repo.all()
    chosen_album = int(id) - 1
    return render_template("single_album.html", album = all_albums[chosen_album])

@app.route('/artists/<id>')
def get_single_artist(id):
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    all_artists = repo.all()
    chosen_artist = int(id) - 1
    return render_template("single_artist.html", artist = all_artists[chosen_artist])

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    all_artists = repo.all()
    return render_template("artists.html", artists = all_artists)


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

#@app.route('/artists', methods = ['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    return "\n".join(
        f"{artist}" for artist in repo.all()
    )

#@app.route('/artists', methods = ['POST'])
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

