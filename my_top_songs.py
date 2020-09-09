# pip3 install requirements.txt
# Shows the top tracks for a user
# Exports:
#   export SPOTIPY_CLIENT_ID=client_id_here
#   export SPOTIPY_CLIENT_SECRET=client_secret_here
#   export SPOTIPY_REDIRECT_URI=redirect_uri_here
# Cannot have two playlists of the same name
import sys
import argparse
import logging
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime
from secrets import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

client_id = SPOTIPY_CLIENT_ID
client_secret = SPOTIPY_CLIENT_SECRET
redirect_uri = SPOTIPY_REDIRECT_URI

def get_args():
    parser = argparse.ArgumentParser(description='Adds track to user playlist')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Playlist to add track to')
    parser.add_argument('-t', '--time', required=True,
                        help='Time Range for songs')
    return parser.parse_args()

def set_sp(scope):
    OAuth = SpotifyOAuth(client_id = client_id, client_secret = client_secret, scope=scope,
                        redirect_uri = redirect_uri, cache_path = '../cache.txt')
    #token = OAuth.get_cached_token()
    sp = spotipy.Spotify(auth_manager=OAuth)
    return sp

def main():
    args = get_args()
    create_user_record_playlist(args)

def create_user_record_playlist(args):
    sp = set_sp('user-top-read')
    #user_range = str(input('short (4 weeks), medium (6 months), or long (years) term?: '))
    print()
    
    
    # To-Do: Add variance in number of songs to add

    user_range = args.time
    if user_range == 'short':
        ranges = [user_range]
    elif user_range == 'medium':
        ranges = ['medium_term']
    elif user_range == 'long':
        ranges = ['long_term']
    else: 
        ranges = ['short_term'] #['short_term', 'medium_term', 'long_term']
    trackIDs = []
    for sp_range in ranges:
        results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
        for i, item in enumerate(results['items']):
            trackIDs.append(item['id'])
                       
    sp = set_sp('playlist-modify-public')

    playlist_name = args.playlist
    playlist_id = str('')

    # To-Do: Add question about creating playlist

    sp.user_playlist_create(sp.me()['id'], playlist_name)
    results = sp.current_user_playlists(limit=50) # limit must stay 50
    for i, item in enumerate(results['items']):
        if item['name'] == playlist_name:
            playlist_id = str(item['id'])

    sp.user_playlist_add_tracks(sp.me()['id'], playlist_id, trackIDs)

if __name__ == '__main__':
    main()
