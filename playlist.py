# this creates a playlist on Spotify based upon songs provided on lines 12-16, can add more.
import spotipy # install spotipy from: https://spotipy.readthedocs.io/
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(
    client_id='', # Create a application @: https://developer.spotify.com/dashboard/applications, here you can get the client id and secret from the page of your created application.
    client_secret='' 
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

playlist_name = 'aaaaaaaaaaaaaaa' # playlist name
playlist_description = 'bnbbbbbbbbbb' # playlist description, can be empty
playlist_id = sp.user_playlist_create(user='', name=playlist_name, public=True, description=playlist_description)['id'] # !!! put the part after https://open.spotify.com/user/ when you copy your spotify link in the username parameter
sp.user_playlist_add_tracks(user='', playlist_id=playlist_id, tracks=recommended_track_uris) # same as last line
