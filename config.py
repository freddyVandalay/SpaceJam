"""
Credentials file
Settings for running playlist app locally
"""

CLIENT_ID = 'ENTER_YOUR_CLIENT_ID'
CLIENT_SECRET = 'ENTER_YOUR_SECRET_ID'
USER_ID = 'ENTER_YOUR_SPOTIFY_USERNAME'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPES = ['user-library-read'
          'playlist-read-private'
          'user-read-private'
          'user-read-email'
          'user-read-birthdate'
          'playlist-modify-public'
          'playlist-modify-private'
          ]

if 'ENTER_YOUR' in CLIENT_ID or 'ENTER_YOUR' in CLIENT_SECRET or 'ENTER_YOUR' in USER_ID:
    raise ValueError('config.py does not contain valid CLIENT_ID, CLIENT_SECRET and USER_ID')
