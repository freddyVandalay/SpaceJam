# SpaceJam (the playlist generator)
Creates a Spotify playlist called Space Jam for the user. Tracks are added to the playlist based on the geolocation of the ISS. ***Work in progress

***Details***
The program uses data from the ISS coordinates to get geolocation from the google maps API. This data is then used as a search phrase to find a track to add to the playlist. It is a work in progress and the target is to add a song from the country which the ISS is above.

Current state doesn't consider if a tack is already in the playlist.
Note: ISS is mainly over water.

***Instructions***
Add your spotify API client id and secret id login.py. Add googlemaps API key on main.py

Run main.py. This will prompt your browser. Copy the callback address and add where asked in terminal.
