from src.utils.auth import get_token, search_for_artist



if __name__ == "__main__":
    

    access_token = get_token()
    artist = search_for_artist(access_token, "Adele")
    print("Artist Info:", artist)

