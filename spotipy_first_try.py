import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# https://open.spotify.com/user/11125633573?si=M0E30eJdQUS4qqVn8iXHzw
# https://open.spotify.com/playlist/08m8krYpkRJko7KHLH9Fpv?si=o84GfeGbTryUSCy-UVzaLg
user_id = "M0E30eJdQUS4qqVn8iXHzw"
playlist_id = "08m8krYpkRJko7KHLH9Fpv?si=o84GfeGbTryUSCy-UVzaLg"

tracks = sp.user_playlist_tracks(user_id, playlist_id)['tracks']

for i, track in enumerate(tracks['items']):
    print("%s;%s;%s;%s" %
          (track['track']['artists'][0]['name'],
           track['track']['name'],
           track['track']['album']['name'],
           # TODO: genre not available - add random genre creator
           track['track']['album']['release_date'].split("-")[0]
           )

          )

# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" %
#               (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
