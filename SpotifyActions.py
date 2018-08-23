import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

import requests

import urllib
import urllib.request as urllib2
import json

class SpotifyActions:
	clientID = "fb91f2209b824af1878ae11118f48932" #client_ID
	secretID = "24ba463a44b74819991dff54d9ac437f" #client Secret key
	userID = "" #spotify username
	token = ""
	scope = 'user-library-read playlist-read-private user-read-private user-read-email user-read-birthdate playlist-modify-public playlist-modify-private' #user privileges
	redirectURI = 'http://localhost:8888/callback'
	headers = {		
			"Accept": "application/json", 
			"Content-Type": "application/json", 
			"Authorization": "Bearer " + token
	}
	
	def __init__(self):
		self.login()


	def login(self):
		client_credentials_manager = SpotifyClientCredentials(client_id=self.clientID, client_secret=self.secretID) 
		self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
		self.generateToken()
		self.headers = {		
			"Accept": "application/json", 
			"Content-Type": "application/json", 
			"Authorization": "Bearer " + self.token
			}
		print(self.token)

	def generateToken(self):
		self.token = util.prompt_for_user_token(self.userID,self.scope,client_id=self.clientID,client_secret=self.secretID,redirect_uri=self.redirectURI)
		if self.token:
			self.sp = spotipy.Spotify(auth=self.token)
		else:
			print("Can't get token for", userID)

	
	def getAllPlaylists(self):
		req = urllib2.Request("https://api.spotify.com/v1/me/playlists", headers = self.headers)
		response = urllib2.urlopen(req)
		obj = json.loads(response.read())
		print(obj)
		print("")
		print("")

	def createPlaylist(self):
		#Create new playlist

		data = {'name' : 'Space Jam', 'description': 'new test list', 'public': False}
		#req = urllib.request.Request(url="https://api.spotify.com/v1/users/userID/playlists", headers=headers, data=data)
		response=requests.post(url="https://api.spotify.com/v1/users/freddyvandalay/playlists", json = data, headers=self.headers)
		print('POST: ')
		print(response)
		print("")
		print("")

	def searchTracks(userSearch):
		userSearch = userSearch.replace(" ", "%20")
		print("search for: " + userSearch)
		req = urllib2.Request("https://api.spotify.com/v1/search?q=" + userSearch +  "&type=track&limit=1", 
						headers= headers
						)
		response = urllib2.urlopen(req)
		results = json.loads(response.read())

		if len(results['tracks']['items']) !=0:
			print(results['tracks']['items'][0]['name'])
			print("")
		else:
			print("no tracks found")
		return results['tracks']['items'][0]['uri']

	def addTrack(trackID):
		data = {'uris' : [trackID], 'position': 0}
		response=requests.post(url="https://api.spotify.com/v1/playlists/0rUhPc3wSr9feqTn9dzvqL/tracks", json= data, headers=headers)
		#print("Playlist: " + str(response))
		print("Added track to playlist: Space Jam" )

	def getToken(): return self.token

