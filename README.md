# Spotify User's Most Listened To
Utilizes Spotipy and Spotify Web API to create playlists of a users's most listened to songs for a certain period of time.

## Requirements
* Spotipy Library https://github.com/plamere/spotipy/tree/2.13.0
* Spotify Account https://www.spotify.com/
* Spotify Developer App/Client ID/Client Secret

# Instructions
1) Install requirements

`pip3 install -r requirements.txt`

2) Collect Spotify Credentials
* Go to your Spotify Developer Dashboard https://developer.spotify.com/dashboard/
* Register a new app
* Collect Client ID and Client Secret (recommended to put into a saved text file along with redirect uri)
* Best results are when using SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'
* Export SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI as environment variables (export ... on mac and set ... on windows)
* Run file from command line with the title of the playlist you want to create as an argument

`python3 my_top_songs.py -p PLAYLIST_NAME`
* Input desired period of time

## ToDo
* Create GUI
* Add additional functionality

# Troubleshooting
* A user cannot have two playlists of the same name
* exporting variables in your environment is critical\

on mac it looks like this:

`export SPOTIFY_CLIENT_ID='YOUR_CLIENT_ID'`

on windows it looks like this:

`set SPOTIFY_CLIENT_ID='YOUR_CLIENT_ID`
