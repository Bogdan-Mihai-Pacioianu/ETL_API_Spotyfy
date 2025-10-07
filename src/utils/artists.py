from src.utils.auth import get_token, get_auth_header


token = get_token()
header  = get_auth_header(token)



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


def search_list_of_artists(token, list_of_artists):
    url = "https://api.spotify.com/v1/artists"
    headers = header
    