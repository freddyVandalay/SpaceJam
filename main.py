"""
This program runs from the terminal and creates a new Spotify playlist called Space Jam.
Tracks are added to the playlist based on the geo-location of the International Space Station, ISS.
By using this program your Spotify account will be modified.
TODO update print statements
TODO move urls to config
"""

import config
import requests
import googlemaps
import urllib.request as urllib2
import json
import login

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": "Bearer " + login.getToken()
}

def get_iss_pos():
	"""
	Format: latitude, longitude
	"""
	req = urllib2.Request(config.ISS_API_ENDPOINT)
	response = urllib2.urlopen(req)
	data = json.loads(response.read())

	return data['iss_position']['latitude'], data['iss_position']['longitude']

def get_google_maps_data(latitude, longitude):
	"""
	Format: latitude, longitude
	"""
	gmaps = googlemaps.Client(key=config.GOOGLE_API_KEY)
	reverse_geocode_result = gmaps.reverse_geocode(longitude, latitude)

	if reverse_geocode_result:
		# print('user_search: {}'.format(reverse_geocode_result[0]['address_components'][0]['long_name']))
		user_search = reverse_geocode_result[0]['address_components'][0]['long_name']
	else:
		user_search = 'ocean' #If no results is found, ISS is over the i ocean

	return user_search

# Spotify actions
def set_user_id():
	req = urllib2.Request("https://api.spotify.com/v1/me", headers=headers)
	response = urllib2.urlopen(req)
	obj = json.loads(response.read())
	user_id = obj['id']

	return user_id

def create_playlist():
	data = {'name' : config.PLAYLIST_NAME,
			'description': config.PLAYLIST_DESCRIPTION,
			'public': config.PLAYLIST_PUBLIC_STATUS}
	response=requests.post(url=config.CREATE_PLAYLIST_ENDPOINT, json= data, headers=headers)
	debug(response)

def get_playlists():
	req = urllib2.Request(config.GET_PLAYLIST_ENDPOINT, headers= headers)
	response = urllib2.urlopen(req)
	playlists = json.loads(response.read())
	# print(playlists['items'][0]['name'])
	# print(playlists['items'][0]['id'])
	# print("")
	return playlists['items']

def get_playlist_id(user__playlists):
	playlist_id = None
	for playlist in user__playlists:
		if playlist['name'] == config.PLAYLIST_NAME:
			print(playlist['id'])
			playlist_id = playlist['id']
			return playlist_id
	return 'not found'


def search_tracks(userSearch):
	userSearch = userSearch.replace(" ", "%20")
	print("Searh phrase: " + userSearch)
	req = urllib2.Request("https://api.spotify.com/v1/search?q=" + userSearch +  "&type=track&limit=1",
						headers= headers
						)
	response = urllib2.urlopen(req)
	results = json.loads(response.read())
	result=''
	if len(results['tracks']['items']) != 0:
		result = results['tracks']['items'][0]['uri']
	else:
		result = "no tracks found"
	print("Search result: " + result)
	return result

def add_track(trackID, playlistID):
	# TODO
	#  - Add track name to print
	#  - string formatting for post request
	data = {'uris' : [trackID], 'position': 0}
	response=requests.post(url="https://api.spotify.com/v1/playlists/" + playlistID + "/tracks",
						   json= data,
						   headers=headers)
	debug(response)
	print("Added track to the Space Jam playlist." )

def debug(response):
	print("Debug: Post " + str(response))

def main():
	print ('Space Jam: A playlist created from space')
	print("Username: " + set_user_id())

	playlist_id = get_playlist_id(get_playlists())

	if playlist_id == 'not found':
		create_playlist()
		playlist_id = get_playlist_id(get_playlists())
		print("Created playlist called: Space Jam")
	else:
		print("Welcome back!")

	lng, lat = get_iss_pos()
	search_phrase = get_google_maps_data(lng, lat)
	track_id = search_tracks(search_phrase)
	add_track(track_id,playlist_id)

if __name__ == "__main__":
	main()


