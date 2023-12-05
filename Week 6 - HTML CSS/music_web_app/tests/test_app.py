from lib.album import Album

def test_albums(web_client):
    response = web_client.post('/albums', data = {
        'title': 'Voyage',
        'release_year': '2022',
        'artist_id': '2'
    })
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ""
    
def test_get_response(web_client):
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Voyage, 2022, 2)"
    

# Test drive get/artists

"""
When get artists is called
A list of all the artists is returned
With a response code of 200
"""

def test_get_artists(web_client):
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Artist 1: Pixies, Rock\n" \
        "Artist 2: ABBA, Pop\n" \
        "Artist 3: Taylor Swift, Pop\n" \
        "Artist 4: Nina Simone, Jazz" 
    
# Test drive post/artists

"""
When post artists is called with
name, genre
Artist is added with no content returned, 200 response code
Then call get to check
"""

def test_get_artists(web_client):
    response = web_client.post("/artists", data = {
        'name': 'Wild nothing',
        'genre': 'Indie'
    })
    assert response.status_code == 200
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Artist 1: Pixies, Rock\n" \
        "Artist 2: ABBA, Pop\n" \
        "Artist 3: Taylor Swift, Pop\n" \
        "Artist 4: Nina Simone, Jazz\n" \
        "Artist 5: Wild nothing, Indie"
