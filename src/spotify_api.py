from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyClient(SpotifyClientCredentials):
    def __init__(self, client_id=None, client_secret=None, proxies=None):
        super().__init__(client_id, client_secret, proxies)

    def _get_client(self):
        pass
    
    def _generate_token(self):
        pass
    