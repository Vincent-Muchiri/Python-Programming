import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify_client_id = ""
spotify_client_secret = ""
spotify_redirect_uri = "http://example.com"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path="data/token.txt"
    )
)
user_id = sp.current_user()["id"]
