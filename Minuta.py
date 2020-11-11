import spotipy
import spotipy.util as util
from secret import client_secret
from pprint import pprint

# Variables
data_limit = 50     # int from 1 to 50

# Constants and inits
redirect_uri = 'http://localhost:8888'
client_id = '27d397bcdc2e4e36a3fedac7941e296a'
username = 'dpalme-mx'
scope = """user-library-read, user-top-read, playlist-read-private,
           playlist-modify-public, playlist-modify-private, user-follow-read"""

# Makes a call to the Spotify API using Spotipy to get the access token
token = util.prompt_for_user_token(username, scope, client_id, client_secret,
                                   redirect_uri)
sp = spotipy.Spotify(auth=token)


def get_top_tracks_spotify():
    """Dictionary with the format {name: uri} using Spotify's internal
    all time top 50 tracks."""

    response = sp.current_user_top_tracks(50, 0, time_range='long_term')
    return {track['uri']: track['name'] for track in response['items']}


def get_top_artists_spotify():
    """Returns a dictionary with the format {name: uri} using Spotify's
    internal all time top 50 artists."""

    response = sp.current_user_top_artists(50, 0, time_range='long_term')
    return {artist['uri']: artist['name'] for artist in response['items']}


def add_tracks(tracks, uri):
    """Adds all give tracks to a playlist.

    :param
      - tracks: List of track uris
      - uri: uri of the playlist """
    if len(tracks) > 100:
        for n in range((len(tracks)//100) + 1):
            sp.user_playlist_add_tracks(username, uri,
                                        tracks[100*n:100*(n+1)])
    else:
        sp.user_playlist_add_tracks(username, uri, tracks)


def replace_track(tracks, uri):
    """Replaces all tracks on a given playlist with a list of tracks.

    :param
      - tracks: List of track uris
      - uri: uri of the playlist """
    if len(tracks) > 100:
        sp.user_playlist_replace_tracks(username, uri, [])
        for n in range(len(tracks)//100):
            sp.user_playlist_add_tracks(username, uri,
                                        tracks[100*n:100*(n+1)])
    else:
        sp.user_playlist_replace_tracks(username, uri, tracks)


def create_playlist(name, privacy=False):
    """Replaces all tracks on a given playlist with a list of tracks.

    :param
      - name: name for the playlist
      - privacy(optional): False for private True for public. False is default
    """
    sp.user_playlist_create(username, name, public=privacy)


if __name__ == "__main__":
    pprint(sp.current_user_top_tracks(1, 0, time_range='short_term'))
