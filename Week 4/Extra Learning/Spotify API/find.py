from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():

    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": 'Basic ' + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}

    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return(token)

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_song(token, song_name, artist_name):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f'?q={song_name}%20artist:{artist_name}&type=track&limit=5'

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    songs = json_result['tracks']['items']
    if len(json_result) == 0:
        return 'No songs found'
    for song in songs:
        print(f"{song['name']} by {song['artists'][0]['name']}")

def search_for_artist(token, artist_name):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f'?q={artist_name}&type=artist&limit=5'

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    artists = json_result['artists']['items']
    if len(json_result) == 0:
        return 'No songs found'
    for artist in artists:
        print(f"{artist['name']} ")
    

token = get_token()
toRun = input('Would you like to search for an artist / song? ')
while toRun.lower() != 'artist' and toRun.lower() != 'song':
    toRun = input('Would you like to search for an artist / song? ')

if toRun.lower() == 'artist':
    search_Artist = input("Who are you looking for? ")
    search_for_artist(token, search_Artist)
else:
    search_Song = input("What are you looking for? ")
    search_Artist = input("Who is it by? ")
    search_for_song(token, search_Song, search_Artist)