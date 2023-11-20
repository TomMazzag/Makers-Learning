from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import webbrowser

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token(auth_code):

    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": 'Basic ' + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": "http://localhost:8888/callback"
    }

    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return(token)

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def user_auth_url():
    authorization_base_url = 'https://accounts.spotify.com/authorize'
    redirect_uri = 'http://localhost:8888/callback'
    scope = 'user-read-private user-read-email' 

    auth_url = (
        authorization_base_url + '?' +
        f'response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}'
    )

    return auth_url

def get_my_profile(token):
    url = 'https://api.spotify.com/v1/me'
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result['id']

def get_playlists(user_ID, token):
    url = f'https://api.spotify.com/v1/users/{user_ID}/playlists'
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result['items']

#print(get_token())
#token = get_token()

webbrowser.open(user_auth_url())
authorization_code = input("Enter the authorization code: ")
token = get_token(authorization_code)
id = get_my_profile(token)
playlists = (get_playlists(id, token))
for x in playlists:
    print(x['name'])