import spotipy
import spotipy.util as util


# Constants and inits
redirect_uri = 'http://localhost:8888'
client_id = 'client_id'
client_secret = 'client_secret'
username = 'username'
scope = """user-library-read, user-top-read, playlist-read-private,
 playlist-modify-public, playlist-modify-private, user-follow-read"""

# Makes a call to the Spotify API using Spotipy to get the access token
token = util.prompt_for_user_token(username, scope, client_id, client_secret,
                                   redirect_uri)
sp = spotipy.Spotify(auth=token)


respuesta = sp.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')
lista_uris = [cancion['uri'] for cancion in respuesta['items']]
sp.user_playlist_create(username, "Top Canciones", public=True)
playlist = sp.current_user_playlists(limit=1)['items'][0]['uri']
sp.user_playlist_add_tracks(username, playlist, lista_uris)
