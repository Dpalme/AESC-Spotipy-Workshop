# AESC-Spotipy-Workshop
# Spotipy: Python y el API de Spotify

## Requerimientos
* [Python 3.X](https://www.python.org/downloads/release/python-376/)
* [Pip](https://pip.pypa.io/en/stable/installing/)
* [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/)
* Cuenta Premium de Spotify


## Spotipy
Librería de interfaces que se comunica directamente con el API de Spotify.

* Simplifica el uso del API.
* No necesitas un servidor.
* Python :)

## Instalación

```
pip install spotipy
```

## Crear aplicación
1. Entra a la [página de desarrolladores de Spotify](https://developer.spotify.com/dashboard/) e inicia sesión con tu cuenta de Spotify.
2. Haz click en el botón **Create an app**.
3. Dale un nombre a tu aplicación y una breve descripción.
4. Haz click en el botón **Edit settings**
5. En la sección **Redirect URIs**, agrega el url`http://localhost:8888`
6. Guarda los cambios hasta abajo de la página

## Obtener tu top 50 canciones
1. Crea un archivo .py
2. importa spotipy
```
import spotipy
import spotipy.util as util
```
3. Agrega las variables de ambiente
```
redirect_uri = 'http://localhost:8888'
client_id = El Client ID en la página de tu aplicación
client_secret = El Client Secret en la página de tu aplicación
username = Tu nombre de usuario
scope = """user-library-read, user-top-read, playlist-read-private,
 playlist-modify-public, playlist-modify-private, user-follow-read"""
```
4. Autorización con Spotify
```
token = util.prompt_for_user_token(username, scope, client_id, client_secret,
                                      redirect_uri)
sp = spotipy.Spotify(auth=token)
```
5. Request a Spotify
```
sp.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')
```
### Variables
#### limit
int de 1 a 50, determina cuántas canciones va a regresar la función.
#### offset
int de 0 a 9223372036854775807 que especifica cuantas canciones se va a "saltar".
#### time_range
Tiene tres opciones:
* `short_term` los últimos 30 días
* `medium_term` los últimos 6 meses
* `long_term` de todo el tiempo
### Respuesta
La función regresa un diccionario con el siguiente formato:
```
{'href': 'https://api.spotify.com/v1/me/top/tracks?limit=20&offset=0&time_range=medium_term',
 'items': [Objetos de canciones],
 'limit': 20,
 'next': 'https://api.spotify.com/v1/me/top/tracks?limit=20&offset=20&time_range=medium_term',
 'offset': 20,
 'previous': None,
 'total': 50}
```
6. Guarda los uri de las canciones
```
lista_uris = []
for cancion in response['items']:
    lista_uris.append(cancion['uri'])
```
o puedes hacer todo eso en una linea
```
lista_uris = [cancion['uri'] for cancion in respuesta['items']]
```
7. Crea una playlist llamada `Top Canciones`
```
sp.user_playlist_create(username, "Top Canciones", public=True)
```
8. Obten su uri
```
playlist = sp.current_user_playlists(limit=1)['items'][0]['uri']
```
9. Agrega las canciones a la playlist
```
sp.user_playlist_add_tracks(username, playlist, lista_uris)
```
