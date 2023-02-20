import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(
    client_id='6108ed3382104746b8afd2cd5a8fd392',
    client_secret='9a097c5f5fad44a99c3e6f8df30163ca'
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

seed_tracks = [
    'spotify:track:3U31Ejeh05Ra3zvPYWU9RA', # Tim and Ginobili - Baby Smoove
    'spotify:track:4LIM4qmpHABufePRrLWbiM', # QKThr - Aphex Twin
    'spotify:track:5ljMlD10En5rRGZU0cs2Np', # aisatsana [102] - Aphex Twin
    'spotify:track:1MXOWbSCEjoGwivtIMnlBV', # Constellations - Duster
    'spotify:track:3gEb5pUrQWdjrdS8gaAyZj', # no love - nappy 01'
]

recommended_tracks = sp.recommendations(seed_tracks=seed_tracks, limit=100)

recommended_track_uris = [track['uri'] for track in recommended_tracks['tracks']]

playlist_name = 'aaaaaaaaaaaaaaa'
playlist_description = 'bnbbbbbbbbbb'
playlist_id = sp.user_playlist_create(user='ggot3fukds46fsau912z4alym', name=playlist_name, public=True, description=playlist_description)['id']
sp.user_playlist_add_tracks(user='ggot3fukds46fsau912z4alym', playlist_id=playlist_id, tracks=recommended_track_uris)