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
    "Authorization": "Bearer {}".format(login.getToken()),
}


def get_iss_pos():
    """
    Format: latitude, longitude
    """
    req = urllib2.Request(config.ISS_API_ENDPOINT)
    response = urllib2.urlopen(req)
    data = json.loads(response.read())

    return data["iss_position"]["latitude"], data["iss_position"]["longitude"]


def get_google_maps_data(latitude, longitude):
    """
    Format: latitude, longitude
    """
    gmaps = googlemaps.Client(key=config.GOOGLE_API_KEY)
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))

    if reverse_geocode_result:
        # print('user_search: {}'.format(reverse_geocode_result[0]['address_components'][0]['long_name']))
        user_search = reverse_geocode_result[0]["address_components"][0]["long_name"]
    else:
        user_search = "ocean"  # If no results is found, ISS is over the i ocean

    return user_search


#  Spotify actions
def describe_user_id():
    req = urllib2.Request("{}/me".format(config.SPOTIFY_BASE_URL), headers=headers)
    response = urllib2.urlopen(req)
    obj = json.loads(response.read())
    user_id = obj["id"]
    return user_id


def create_playlist():
    data = {
        "name": config.PLAYLIST_NAME,
        "description": config.PLAYLIST_DESCRIPTION,
        "public": config.PLAYLIST_PUBLIC_STATUS,
    }

    url = config.SPOTIFY_BASE_URL + config.PLAYLIST_ENDPOINT
    response = requests.post(url=url, json=data, headers=headers)
    # debug(response)


def get_playlists():
    url = config.SPOTIFY_BASE_URL + config.PLAYLIST_ENDPOINT
    req = urllib2.Request(url=url, headers=headers)
    response = urllib2.urlopen(req)
    playlists = json.loads(response.read())
    # print(playlists['items'][0]['name'])
    # print(playlists['items'][0]['id'])
    return playlists["items"]


def get_playlist_id(user_playlists):
    for playlist in user_playlists:
        if playlist["name"] == config.PLAYLIST_NAME:
            # debug(playlist['id'])
            playlist_id = playlist["id"]
            return playlist_id
    return "not found"


def search_tracks(user_search):
    user_search = user_search.replace(" ", "%20")
    print("Track search phrase: " + user_search)

    req = urllib2.Request(
        "{0}/search?q={1}&type=track&limit=1".format(
            config.SPOTIFY_BASE_URL, user_search
        ),
        headers=headers,
    )

    response = urllib2.urlopen(req)
    results = json.loads(response.read())
    if len(results["tracks"]["items"]) != 0:
        result = results["tracks"]["items"][0]["uri"]
    else:
        result = "no tracks found"
    print("Search result: " + result)
    return result


def add_track(track_id, playlist_id):
    # TODO
    #  - Add track name to print
    if not track_exist(track_id, playlist_id):
        data = {"uris": [track_id], "position": 0}
        requests.post(
            url="{}/playlists/{}/tracks".format(config.SPOTIFY_BASE_URL, playlist_id),
            json=data,
            headers=headers,
        )
        print("Added new track to playlist.")


def track_exist(new_track_id, playlist_id):
    url = config.SPOTIFY_BASE_URL + "/playlists/{}/tracks".format(
        playlist_id, new_track_id
    )
    req = urllib2.Request(url=url, headers=headers)
    response = urllib2.urlopen(req)
    result = json.loads(response.read())
    tracks = result["items"]
    for track in tracks:
        track_id = track["track"]["id"]
        if new_track_id.split(":")[2] == track_id:
            print("Adding track failed. Track already exists")
            return True
    return False


def main():
    print("Space Jam: A playlist created from space")
    print("Logged in as: " + describe_user_id())

    playlist_id = get_playlist_id(get_playlists())

    if playlist_id == "not found":
        create_playlist()
        playlist_id = get_playlist_id(get_playlists())
        print("Created playlist called: Space Jam")
    else:
        print("Welcome back!")

    lng, lat = get_iss_pos()
    search_phrase = get_google_maps_data(lng, lat)
    track_id = search_tracks(search_phrase)
    add_track(track_id, playlist_id)


if __name__ == "__main__":
    main()
