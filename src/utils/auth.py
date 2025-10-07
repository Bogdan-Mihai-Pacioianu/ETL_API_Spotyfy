from requests import post, get
from requests.exceptions import HTTPError
import os
import base64
from urllib.parse import quote

from dotenv import load_dotenv

load_dotenv()



SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET= os.getenv("CLIENT_SECRET")
SPOTIFY_REDIRECTED_URI = os.getenv("REDIRECTED_URI")


def get_token():
    url = "https://accounts.spotify.com/api/token"

    auth_string = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    response = post(url, headers=headers, data=data)
    json_result = response.json()

    # Handle potential errors
    if response.status_code != 200:
        raise HTTPError(f"Failed to get token: {json_result}")
    return json_result["access_token"]


def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    encoded_artist_name = quote(artist_name)
    query = f"?q={encoded_artist_name}&type=artist&limit=1"
    query_url = url + query

    response = get(query_url, headers=headers)
    json_result = response.json()

    if "artists" not in json_result:
        print("No artist found or invalid token.")
        return None

    artist_items = json_result["artists"]["items"]
    if len(artist_items) == 0:
        print("Artist not found.")
        return None

    return artist_items 

