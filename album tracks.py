import spotipy
from spotipy import SpotifyOAuth

client_id = '63bbafc106744068bf3456c016af2308'
client_secret = '6530bfea585242c0b0071b4d6531eef0'
redirect_uri = 'https://localhost/'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri, scope='playlist-modify-private'))
username='ggot3fukds46fsau912z4alym'
desc='for real'
title='cornelius von blasphemore'
public=False
playlist = sp.user_playlist_create(name=title,description=desc,public=public,user=username)
add_song = sp.playlist_add_items(playlist_id=playlist['id'],items=['spotify:track:62OqqOKP1mJLJaz69U4N6h','1Pvn1rrZaY1QePkIBnOklS'])
list1 = sp.artists(['spotify:artist:1IOfE2EZJLsJ5H87ucZmrq','spotify:artist:7tYKF4w9nC0nq9CsPZTHyP','spotify:artist:5AyEXCtu3xnnsTGCo4RVZh','spotify:artist:1TIbqr0x8HoKzKBNtNN8wf','spotify:artist:2xvtxDNInKDV4AvGmjw6d1'])
list2 = sp.tracks(['spotify:track:2wiV5iKq5F5A0KUee4OrlK','spotify:track:1OubIZ0ARYCUq5kceYUQiO','spotify:tracks:2Bc4llhjJBW77I552RgA3L'])
songs = sp.recommendations(seed_artists=list1,seed_tracks=list2, limit=100)
track_uris = [track['uri'] for track in songs['tracks']]
sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)