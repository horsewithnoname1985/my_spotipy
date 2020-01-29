import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials


def get_random_genre(lang):
    if lang == "czech":
        genres = ["Rock", "Pop", "House", "Hip-Hop", "Klasická", "R&B", "Džez",
                  "Metal"]

    if lang == "thai":
        genres = ["ร็อค", "ป๊อบ", "บ้าน", "ฮิบ-ฮอบ", "คฺลาด-สิก",
                  "อาร์แอนด์บี", "แจ็ส", "Metal"]
    else:
        genres = ["Rock", "Pop", "House", "Soundtrack", "Hip-Hop", "Classic",
                  "R&B", "Jazz", "Metal"]

    return random.choice(genres)


if __name__ == '__main__':

    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    # https://open.spotify.com/user/11125633573?si=M0E30eJdQUS4qqVn8iXHzw
    # https://open.spotify.com/playlist/08m8krYpkRJko7KHLH9Fpv?si=o84GfeGbTryUSCy-UVzaLg
    # https://open.spotify.com/playlist/70ANdI7a9xTCTICgpvOkL8?si=H83IS22IS3SA_83hO4hnqA
    # https://open.spotify.com/playlist/70ANdI7a9xTCTICgpvOkL8?si=7T-a0rVQTE-Lv91HWWa3ew
    # https://open.spotify.com/playlist/0zFJYziDwEAVmGLqvMbmde?si=R0TT76nAQEmwi-VCnIYeHQ
    # https://open.spotify.com/playlist/3F1ZgOApK9ngsemuDzZrH0?si=4FUArpuaRnSBghXVGGZwcw
    user_id = "M0E30eJdQUS4qqVn8iXHzw"
    playlist_id = "2l3CU7QId7ckcLzR2GFjTA?si=jxTjlgwhQtywsdAQHRXSgg"

    tracks = sp.user_playlist_tracks(user_id, playlist_id, limit=100)['tracks']

    for i, track in enumerate(tracks['items']):
        print("%s;%s;%s;%s;%s;%s" %
              (track['track']['artists'][0]['name'],
               track['track']['name'],
               track['track']['album']['name'],
               track['track']['artists'][0]['name'],
               get_random_genre("polish"),
               track['track']['album']['release_date'].split("-")[0]
               )
              )
