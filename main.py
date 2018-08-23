#This program runs from the terminal and creates a new spotify playlist called Space Jam. 
#Tracks are added to the playlist based on the geolocation of the Internatinal Space Station, ISS. 
#By using this program your spotify account will be modfied. (New playlist will be created and song added to the playlist)
										
										
import requests
import googlemaps
import urllib
import urllib.request as urllib2
import json
import login
from datetime import datetime


gmaps = googlemaps.Client(key='AIzaSyDm89bpm5JuWByGYeExMKtk-VDADwtCX_8') #Add googleAPI key

token = login.getToken()
headers = {		
			"Accept": "application/json", 
			"Content-Type": "application/json", 
			"Authorization": "Bearer " + token
}

def getISSPos():
	req = urllib2.Request("http://api.open-notify.org/iss-now.json")
	response = urllib2.urlopen(req)
	data = json.loads(response.read())
	lng = data['iss_position']['longitude']
	lat = data['iss_position']['latitude']

	return lng,lat

def getGoogleMapsData(lng,lat):
	reverse_geocode_result = gmaps.reverse_geocode((lat, lng))

	if reverse_geocode_result:
		#print('City: ' + reverse_geocode_result[0]['address_components'][0]['long_name'])
		userSearch = reverse_geocode_result[0]['address_components'][0]['long_name']
	else:
		userSearch = 'ocean' #If no results is found, ISS is over the i ocean
		return 'ocean'

	return userSearch

###Spotify actions
def setUserID():
	req = urllib2.Request("https://api.spotify.com/v1/me", headers=headers)
	response = urllib2.urlopen(req)

	obj = json.loads(response.read())
	userID = obj['id']
	return userID

def createPlaylist():
	data = {'name' : 'Space Jam', 'description': 'new test list', 'public': False}
	response=requests.post(url="https://api.spotify.com/v1/users/freddyvandalay/playlists", json= data, headers=headers)
	debug(response)

def getPlaylists():
	req = urllib2.Request("https://api.spotify.com/v1/me/playlists", headers= headers)
	response = urllib2.urlopen(req)
	playlists = json.loads(response.read())
	#print(playlists['items'][0]['name'])
	#print(playlists['items'][0]['id'])
	#print("")
	return playlists['items']

def playlistExist(userPlaylists):
	playlistID=''
	for playlist in userPlaylists:
		if playlist['name'] == 'Space Jam':
			print(playlist['id'])
			playlistID = playlist['id']
			return True
		print('not found')
	return False

def getPlaylistID(userPlaylists):
	for playlist in userPlaylists:
		if playlist['name'] == 'Space Jam':
			print(playlist['id'])
			playlistID = playlist['id']
			return playlistID
	return 'not found'


def searchTracks(userSearch):
	userSearch = userSearch.replace(" ", "%20")
	print("Searh phrase: " + userSearch)
	req = urllib2.Request("https://api.spotify.com/v1/search?q=" + userSearch +  "&type=track&limit=1", 
						headers= headers
						)
	response = urllib2.urlopen(req)
	results = json.loads(response.read())
	result=''
	if len(results['tracks']['items']) !=0:
		result = results['tracks']['items'][0]['uri']
	else:
		result = "no tracks found"
	print("Search result: " + result)
	return result

def addTrack(trackID, playlistID):

	print
	data = {'uris' : [trackID], 'position': 0}

	response=requests.post(url="https://api.spotify.com/v1/playlists/" + playlistID + "/tracks", json= data, headers=headers)
	
	debug(response)
	print("Added track to the Space Jam playlist." )

def debug(response):
	print("Debug: Post " + str(response))

def main():
	#OAuth token
	print ('Welcome to Space Jam: A playlist created from space')
	print("Username: " + setUserID())

	playlistID = getPlaylistID(getPlaylists())

	if playlistID == 'not found':
		createPlaylist()
		playlistID = getPlaylistID(getPlaylists())
		print("Created playlist called: Space Jam")
	else:
		print("Welcome back!")

	lng,lat = getISSPos()

	searchPhrase = getGoogleMapsData(lng,lat)
	
	trackID = searchTracks(searchPhrase)

	addTrack(trackID,playlistID)

if __name__ == "__main__":
    main()


