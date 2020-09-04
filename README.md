# Spotify User's Most Listened To
Utilizes Spotipy and Spotify Web API to create playlists of a users's most listened to songs for a certain period of time.

## Requirements
* Spotipy Library https://github.com/plamere/spotipy/tree/2.13.0
* Spotify Account https://www.spotify.com/
* Spotify Developer App/Client ID/Client Secret

# Instructions
1) Install spotipy
'pip3 install spotipy'

2) Collect Spotify Credentials
* Go to your Spotify Developer Dashboard https://developer.spotify.com/dashboard/
* Register a new app
* Collect Client ID and Client Secret (recommended to put into a saved text file along with redirect uri)
* Best results are when using SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'
* Export SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI as environment variables (export ... on mac and set ... on windows)
* Run file from command line with the title of the playlist you want to create as an argument
'python3 my_top_songs.py -p PLAYLIST_NAME'
* Input desired period of time

## ToDo
* Create GUI
* Add additional functionality

# Troubleshooting
* A user cannot have two playlists of the same name
