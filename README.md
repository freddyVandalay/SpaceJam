# SpaceJam - the Spotify playlist generator 

This program creates a Spotify playlist called SpaceJam. 
Tracks are added to the playlist based on the geolocation of the ISS (International Space Station).

*Note: This is a work in progress*
##### Details
The idea is to get the coordinates of the current ISS position
and use this to create a keyword to search for a track on Spotify.
The track is then added to the SpaceJam playlist. 

The program creates the playlist if it doesn't already exists. 

Note: ISS is mainly over water.

##### USAGE
Add your api credentials to the config file

Run main.py. This will prompt your browser. Copy the callback address and add where asked in terminal.

#### API Resources
ISS API:
http://open-notify.org/Open-Notify-API/ISS-Location-Now/

Spotify API:
https://developer.spotify.com/documentation/web-api/


###### TODO
 - Write a version of the program to be executed with an aws lambda function.
 - Current state doesn't consider if a tack is already in the playlist.
 - General clean-up and improvement of code
 - Update Usage section
