import spotipy
from spotipy.oauth2 import SpotifyOAuth


with open('parameters.txt', 'r') as p:
    parameters = p.readlines()

    cli_id = parameters[0]
    cli_sec = parameters[1]
    red_uri = parameters[2]
    device = parameters[3]





scope = 'user-modify-playback-state user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cli_id,
                                               client_secret=cli_sec,
                                               redirect_uri=red_uri,
                                               scope=scope))



#---TOPARTISTS: Grabs currently most listened to artists---#
def topArtists() -> list:
    artists = []
    results = sp.current_user_top_artists(limit=10, offset=0, time_range='medium_term')
    for idx, item in enumerate(results['items']):
        artists.append(item['name'])
    return '\n'.join(artists)

def resumeSong():
    sp.start_playback(device_id=device)
    return 'Music Resumed'

def pauseSong():
    sp.pause_playback(device_id=device)
    return 'Music Paused'


print('Enter on of the three values:\n1: Top Artists\n2: Resume Music\n3: Pause Music:\n4: Exit program\n')
while True:
    choice = int(input('Make a choice: '))

    if choice == 1:
        print(topArtists())
    if choice == 2: 
        print(resumeSong())
    if choice == 3: 
        print(pauseSong())
    if choice == 4:
        exit()