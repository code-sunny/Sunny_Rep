from dotenv import load_dotenv

load_dotenv()

import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret
)

sp = spotipy.Spotify(auth_manager=auth_manager)
