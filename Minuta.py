import spotipy
import spotipy.util as util
from pprint import pprint
from collections import defaultdict

# Constantes para autorización
redirect_uri = 'http://localhost:8888'
client_id = 'client_id'
client_secret = 'client_secret'
username = 'username'
scope = """user-library-read, user-top-read, playlist-read-private,
 playlist-modify-public, playlist-modify-private, user-follow-read"""

# Autorización con Spotify
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
sp = spotipy.Spotify(auth=token)

# Crear Playlist Top 50
respuesta = sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')
lista_uris = [cancion['uri'] for cancion in respuesta['items']]
sp.user_playlist_create(username, "Top Canciones", public=True)
playlist = sp.current_user_playlists(limit=1)['items'][0]['uri']
sp.user_playlist_add_tracks(username, playlist, lista_uris)

# Separar canciones por género
canciones_uri = {cancion['name']: cancion['artists'][0] for cancion in lista_canciones}
generos = defaultdict(list)
for cancion, artist in canciones_uri.items():
    obj_artista = sp.artist(artist['uri'])
    for genre in obj_artista['genres']:
        generos[genre].append(str(artist['name']) + "-" + str(cancion))

pprint(generos)
