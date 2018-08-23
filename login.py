import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util



clientID ="{you-client-id}" #add client_ID
secretID = "{your-secrey-id}" #add client Secret key
userID = "" #spotify username

client_credentials_manager = SpotifyClientCredentials(client_id=clientID, client_secret=secretID) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

scope = 'user-library-read playlist-read-private user-read-private user-read-email user-read-birthdate playlist-modify-public playlist-modify-private' #user previligies

token = util.prompt_for_user_token(userID,scope,client_id=clientID,client_secret=secretID,redirect_uri='http://localhost:8888/callback')

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", userID)

def getToken(): return token

#set SPOTIPY_CLIENT_ID='fb91f2209b824af1878ae11118f48932'
#set SPOTIPY_CLIENT_SECRET='24ba463a44b74819991dff54d9ac437f'
#set SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'