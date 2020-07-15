import json
import requests
from secrets import spotify_user_id, spotify_token



class CreatePlaylist:

	def __init__(self):
		self.user_id = spotify_user_id

	#Step 1: Log in to youtube.
	def get_youtube_client(self):
		pass

	#Step 2: Grab liked videos.
	def get_liked_videos(self):
		pass

	# Step 3: Create new playlist.
	def create_playlist(self):

		# Create a new playlist
		request_body = json.dumps({
			"name" : "Youtube favourites",
			"description" : "Liked Youtube songs",
			"public" : True
			})

		query = "https://api.spotify.com/v1/users/{}/playlists".format(
			spotify_user_id)
		response = requests.post(
			query,
			data=request_body,
			headers={
				"Content-Type":"application/json",
				"Authorization":"Bearer {}".format(spotify_token)
			}
		)
		response_json = response.json()

		# Playlist ID
		return response_json("id")

	#Step 4: Search for the song.
	def get_spotigy_uri(self, song_name, artist):
		# search for the song
		query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
			song_name,
			artist
		)
		response = requests.get(
			query,
			headers={
				"Content-Type": "application/json",
				"Authorization": "Bearer {}".format(spotify_token)
			}
		)
		response_json = response.json()
		songs = response_json["tracks"]["items"]

		#only use the first song
		uri = songs[0]["uri"]

		return uri

	# Step 5: Add the song into spotify playlist.
	def add_song_to_playlist(self):
		pass



