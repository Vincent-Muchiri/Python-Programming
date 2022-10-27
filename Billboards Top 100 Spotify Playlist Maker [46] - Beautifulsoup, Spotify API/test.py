import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify_client_id = "b5025c8690214771b0add8d0d5f0c1ee"
spotify_client_secret = "c2cccc65b1234d0c809efe8cdfacec14"
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
