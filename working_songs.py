# Shows the top tracks for a user
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime

scope = 'user-top-read'
OAuth = SpotifyOAuth(scope=scope,
                     redirect_uri='http://localhost:8888/callback/',
                     cache_path='../cache.txt')
token = OAuth.get_cached_token()

sp = spotipy.Spotify(auth_manager=OAuth)
ranges = ['short_term', 'medium_term', 'long_term']
trackIDs = []

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=10)
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['artists'][0]['name'])
        trackIDs.append(item['id'])
    print()
    
scope = 'playlist-modify-public'
OAuth = SpotifyOAuth(scope=scope,
                     redirect_uri='http://localhost:8888/callback/',
                     cache_path='../cache.txt')
                     
sp = spotipy.Spotify(auth_manager=OAuth) 
playlist_name = str('test')
playlist_id = str('')
sp.user_playlist_create(sp.me()['id'], playlist_name)
results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    if item['name'] == playlist_name:
        playlist_id = str(item['id'])
        
print(playlist_id)
print(trackIDs[1])

sp.user_playlist_add_tracks(sp.me()['id'], playlist_id, trackIDs)