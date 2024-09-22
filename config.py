# refactor to work with .env file
SCOPES = [
    "user-library-read",
    "playlist-read-private",
    "user-read-private",
    "user-read-email",
    "user-read-birthdate",
    "playlist-modify-public",
    "playlist-modify-private",
]

PLAYLIST_NAME = "Space Jam"
PLAYLIST_DESCRIPTION = (
    "A out ouf this world playlist. "
    "A playlist created from space. "
    "A playlist generated using the geo-location of the International Space Station"
)
PLAYLIST_PUBLIC_STATUS = False

USER_ID = ""
SPOTIFY_BASE_URL = "https://api.spotify.com/v1"
PLAYLIST_ENDPOINT = "/users/{}/playlists".format(USER_ID)  # TODO
ISS_API_ENDPOINT = "http://api.open-notify.org/iss-now.json"
