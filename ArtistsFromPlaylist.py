
import spotipy

from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",client_secret="",scope=scope, redirect_uri=""))

artists = {}

# This script gathers all of the artists in a list and sorts them by the amount of songs on the list
# Requires API keys (client_id, client_secret) as well as the playlist id
# Prints list into output.txt

def process_tracks(items):
    for idx, item in enumerate(items):
        track = item['track']
        artist_name = track['artists'][0]['name']

        if artist_name not in artists:
            artists[artist_name] = 1
        else:
            artists[artist_name] += 1




playlists = sp.current_user_playlists(limit=100)

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

playl = sp.playlist_items(playlist_id="")

process_tracks(playl['items'])

while playl['next']:
    playl = sp.playlist_items(playlist_id="", offset=playl['offset'] + len(playl['items']))  # Fetch the next page of tracks
    process_tracks(playl['items'])  # Process the tracks on the current page



with open("output.txt", "w", encoding="utf-8") as file1:
    for artist, count in sorted(artists.items(), key=lambda x:x[1], reverse=True):
        file1.write(f"{artist}: {count} songs \n")
