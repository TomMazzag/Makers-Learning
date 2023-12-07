import os
from flask import Flask, request, render_template, redirect, url_for
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
    chosen_album = repo.find(id)
    return render_template("single_album.html", album = chosen_album)

@app.route('/albums/delete/<id>')
def delete_album(id):
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    repo.delete(id)
    return redirect(url_for('get_albums'))

@app.route('/albums/new', methods = ['GET'])
def add_new_album():
    return render_template("new_album.html")

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

@app.route('/artists/new', methods = ['GET'])
def add_new_artist():
    return render_template("new_artist.html")


@app.route('/albums', methods = ['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    form = request.form

    if form['title'] == '' or form['release_year'] == '' or form['artist_id'] == '':
        error = 'There was an error in your submission, one or more of the fields is empty'
        return render_template("new_album.html", errors=error)

    album = Album(None, 
                  form['title'],
                  form['release_year'],
                  form['artist_id'])
    repo.create(album)
    return redirect(f"/albums/{album.id}")

#@app.route('/artists', methods = ['GET'])
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
    form = request.form
    if form['name'] == '' or form['genre'] == '':
        error = 'There was an error in your submission, one or more of the fields is empty'
        return render_template("new_artist.html", errors=error)
    
    artist = Artist(None,
                       form['name'],
                       form['genre'])
    repo.create(artist)
    return redirect(f"/artists/{artist.id}")


from example_routes import apply_example_routes
apply_example_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

