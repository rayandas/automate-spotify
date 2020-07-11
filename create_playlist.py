import json
import requests
from secrets import spotify_user_id, spotify_token


class CreatePlaylist:

    def __init__(self):
	    self.user_id = spotify_user_id

    #Log in to youtube.
    def get_youtube_client(self):
	    pass

    #Grab liked videos.
    def get_liked_videos(self):
	    pass

	#Create new playlist.
    def create_playlist(self):

    	# Create a new playlist
    	request_body = json.dumps({
    		"name" : "Youtube favourites",
    		"description" : "Liked Youtube songs",
    		"public" : True
    		})

    	query = "https://api.spotify.com/v1/users/{}/playlists".format(
    		spotify_user_id)

    #Search for the song.
    def get_spotigy_uri(self):
    	pass

    #add the song into spotify playlist.
    def add_song_to_playlist(self):
    	pass



