import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import config


client_credentials_manager = SpotifyClientCredentials(
    client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = util.prompt_for_user_token(
    config.USER_ID,
    config.SCOPES,
    client_id=config.CLIENT_ID,
    client_secret=config.CLIENT_SECRET,
    redirect_uri=config.REDIRECT_URI,
)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for {}".format(config.USER_ID))


def getToken():
    return token
