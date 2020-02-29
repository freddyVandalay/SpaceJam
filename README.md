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

#### Creating a virtual environment
```bash
python3 -m venv .venv
```

#### Activating the newly created virtual environment

You always want your virtual environment to be active when working on this project.

```bash
source ./.venv/bin/activate
```

#### Installing Python requirements

This will install some of the packages you might find useful:

```bash
pip3 install -r ./requirements.txt
```

##### Create config file
1. Rename config.template.py --> config.py
2. and add required credentials

.gitignore will exclude config.py in future commits.

#### API Resources
ISS API:
http://open-notify.org/Open-Notify-API/ISS-Location-Now/

Spotify API:
https://developer.spotify.com/documentation/web-api/


###### TODO
 - Write a version of the program to be executed with an aws lambda function.
 - Current state doesn't consider if a track is already in the playlist.
 - General clean-up and improvement of code
