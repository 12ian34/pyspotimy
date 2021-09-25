import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# get secrets
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_SECRET')
SPOTIFY_CLIENT_CALLBACK_URI = os.environ.get('SPOTIFY_CB_URI')

# initialise spotipy client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_CLIENT_CALLBACK_URI,
        # scope="user-library-read",
        # scope="user-read-recently-played",
        scope="user-top-read",
    )
)


def get_top_tracks_data(term):

    # set initial variables
    top_tracks = {}
    rank = 1

    # validate term
    if term in ['short', 'medium', 'long']:
        print('chosen term: {}'.format(term))
    else:
        print('ERROR: invalid term. Pick "short", "medium" or "long"')
        # raise.sysExit()

    # fetch top tracks via spotipy client
    response = sp.current_user_top_tracks(
        limit=100,
        offset=0,
        time_range='{}_term'.format(term)
    )

    # parse response data into new dict
    for item in response['items']:
        top_tracks[rank] = {}

        artists = ', '.join([artist['name'] for artist in item['artists']])
        title = item['name']

        top_tracks[rank]['artist'] = artists
        top_tracks[rank]['title'] = title

        # print out each top track
        print('{} - {} - {} - {}'.format(term, rank, artists, title))

        rank += 1

    return top_tracks


# run for each term
top_tracks_short_term = get_top_tracks_data('short')
top_tracks_medium_term = get_top_tracks_data('medium')
top_tracks_long_term = get_top_tracks_data('long')

# current_user = sp.current_user()
# results = sp.current_user_saved_tracks()

# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
