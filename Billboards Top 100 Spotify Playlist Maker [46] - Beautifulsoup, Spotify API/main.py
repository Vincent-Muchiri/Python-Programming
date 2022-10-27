from datetime import datetime
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
import json

wrong_entry = True
while wrong_entry:
    # TODO Prompt the user to enter a date
    release_date_string = input("Which date would you like to travel to? Enter in the format YYYY-MM-DD: ")

    try:
        # TODO Get the current date object and convert the response to a date object
        current_date_obj = datetime.today().date()
        response_date_obj = datetime.strptime(release_date_string, "%Y-%m-%d").date()

    except ValueError:
        print("Please enter a value in the format YYYY-MM-DD")
        pass
    else:
        # TODO Validate the date and make sure it's not in the future
        if response_date_obj > current_date_obj:
            print("Please enter a date in the past")
        else:
            print("Sending request to Billboard.com...")
            wrong_entry = False

# TODO Make a request to Billboard and get the HTML text
# url = f"https://www.billboard.com/charts/hot-100/{release_date_string}/"
# response = requests.get(url)
# billboard_html_text = response.text

# TODO Offline testing
with open("data/1999-08-21.html", mode="r", encoding="utf8") as html_file:
    billboard_html_text = html_file.read()

# TODO Create the beautifulsoup class
billboard_soup = BeautifulSoup(billboard_html_text, "html.parser")
# print(billboard_soup.title)

# TODO Get the song titles
print("Scraping song titles from Billboard.com...")
# selected = billboard_soup.select(selector="li h3")
selected = billboard_soup.find_all(name="h3", class_="a-no-trucate")
music_titles = []
for selection in selected:
    title = selection.getText().strip("\n\t")
    # print(title)
    music_titles.append(title)

# print(music_titles)

# TODO Get the artist names
print("Scraping artist names from Billboard.com...")
selections = billboard_soup.find_all(name="span", class_="a-font-primary-s")
artist_names = []
for selection in selections:
    text = selection.getText()
    text = text.strip("\n\t")

    if text == "NEW" or text == "RE-\nENTRY" or text == "-" or text == "RIAA Certification:":
        pass
    else:
        artist_name = text
        # print(artist_name)
        artist_names.append(artist_name)

# TODO Test Data
# print(len(music_titles), len(artist_names))
# print(music_titles)
# print(artist_names)
# music_titles = ['Honey', 'Mo Money Mo Problems', 'Quit Playing Games (With My Heart)', 'How Do I Live', '2 Become 1', 'You Make Me Wanna...', "I'll Be Missing You", 'Semi-Charmed Life', 'Barbie Girl', 'Never Make A Promise', 'All For You', 'Foolish Games/You Were Meant For Me', 'Not Tonight', 'Up Jumps Da Boogie', 'Invisible Man', 'Do You Know (What It Takes)', 'Sunny Came Home', 'Building A Mystery', 'Bitch', 'All Cried Out', 'Coco Jamboo', 'C U When U Get There (From "Nothing To Lose")', 'Return Of The Mack', 'Someone', 'I Miss My Homies', 'The Freshmen', 'What About Us', "You Should Be Mine (Don't Waste Your Time)", 'Barely Breathing', 'G.H.E.T.T.O.U.T.', 'Gotham City', 'For You I Will (From "Space Jam")', "Say You'll Be There", 'Do You Like This', 'All I Want (From "GOOD Burger")', "Hard To Say I'm Sorry", 'ESPN Presents The Jock Jam', 'More Than This', 'My Love Is The Shhh!', 'MMMBop', 'Backyard Boogie', 'I Say A Little Prayer', 'I Want You', "It's Your Love", "I Care 'Bout You", 'Take It To The Streets', 'I Can Love You', '6 Underground', 'To The Moon And Back', 'Look Into My Eyes (From "Batman & Robin")', 'After 12, Before 6', 'When I Die', 'Go The Distance (From "Hercules")', 'Big Bad Mamma (From "Def Jam\'s How To Be A Player")', 'You Light Up My Life', "Things Just Ain't The Same", 'I Wanna Be There', 'To Make You Feel My Love', 'Hole In My Soul', 'Butta Love', 'As We Lay', 'No Tengo Dinero', 'Smile', 'Have A Little Mercy', 'Whatever', 'Around The World', 'Alone', 'Fix', 'Down For Yours', 'Need Your Love', "Don't Say", 'You Bring Me Up', "Can't Let Go", 'Piece Of My Heart', 'Jack-Ass', "It's Alright", 'Rhythm Of Love', 'Never, Never Gonna Give You Up', 'Tubthumping', 'When You Talk About Love', 'Supernatural', 'Happy With You', 'Four Leaf Clover', 'Can U Feel It', 'Butterfly Kisses', 'Legend Of A Cowgirl', "Smokin' Me Out", 'We Can Get Down', 'Can We (From "Booty Call")', "It's No Good", 'Men Of Steel (From "Steel")', "I'm Not A Fool", "Can't Get You Out Of My Mind", 'Drink, Swear, Steal & Lie', 'Relax & Party', 'In A Dream', 'Thinking Of You', "What's Stopping You", 'Free', 'Don\'t Wanna Be A Player (From "Booty Call")']
# artist_names = ['Mariah Carey', 'The Notorious B.I.G. Featuring Puff Daddy & Mase', 'Backstreet Boys', 'LeAnn Rimes', 'Spice Girls', 'Usher', 'Puff Daddy & Faith Evans Featuring 112', 'Third Eye Blind', 'Aqua', 'Dru Hill', 'Sister Hazel', 'Jewel', "Lil' Kim Feat. Da Brat, Left Eye, Missy Elliott & Angie Mar", 'Magoo And Timbaland', '98 Degrees', 'Robyn', 'Shawn Colvin', 'Sarah McLachlan', 'Meredith Brooks', 'Allure Featuring 112', 'Mr. President', 'Coolio Featuring 40 Thevz', 'Mark Morrison', 'SWV (Featuring Puff Daddy)', 'Master P Featuring Pimp C And The Shocker', 'The Verve Pipe', 'Total', 'Brian McKnight Featuring Mase', 'Duncan Sheik', 'Changing Faces', 'R. Kelly', 'Monica', 'Spice Girls', 'Rome', 'Az Yet Featuring Peter Cetera', 'Various Artists', '10,000 Maniacs', "Somethin' For The People Featuring Trina & Tamara", 'Hanson', 'Mack 10', 'Diana King', 'Savage Garden', 'Tim McGraw With Faith Hill', 'Milestone', 'Rampage Featuring Billy Lawrence', 'Mary J. Blige', 'Sneaker Pimps', 'Savage Garden', 'Bone Thugs-N-Harmony', 'Sam Salter', 'No Mercy', 'Michael Bolton', 'Foxy Brown Featuring Dru Hill', 'LeAnn Rimes', 'Deborah Cox', 'Blessid Union Of Souls', 'Billy Joel', 'Aerosmith', 'Next', 'Dana', 'Los Umbrellos', 'Scarface Featuring 2Pac & Johnny P', '4.0', 'En Vogue', 'Daft Punk', 'Bee Gees', "BLACKstreet With Special Guests Ol' Dirty Bastard & Slash", 'Nastyboy Klick Featuring Roger Troutman', 'Big Bub Featuring Queen Latifah & Heavy D', 'Jon B', 'K-Ci & JoJo', 'Laurnea', 'Shaggy (Featuring Marsha)', 'Beck', 'Queen Latifah', 'DJ Company', 'Lisa Stansfield', 'Chumbawamba', 'Patti LaBelle', 'Wild Orchid', 'Samantha Cole', 'Abra Moore', '3rd Party', 'Raybon Bros.', 'Imani Coppola', 'Warren G Featuring Ronald Isley', 'Myron', 'SWV', 'Depeche Mode', "Shaquille O'Neal, Ice Cube, B Real, Peter Gunz & KRS-One", 'Immature', 'Lil Suzy', 'Michael Peterson', 'Ivory', 'Rockell', 'Tony Toni Tone', "The O'Jays", 'Ultra Nate', 'Joe']


import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

# TODO Create a spotify account and log in to the developer section on https://developer.spotify.com/dashboard/
# spotify_client_id = "Get your client id after creating the developer account"
# spotify_client_secret = "Get your client id after creating the developer account"
spotify_client_id = "b5025c8690214771b0add8d0d5f0c1ee"
spotify_client_secret = "c2cccc65b1234d0c809efe8cdfacec14"
spotify_redirect_uri = "http://example.com"  # Other reserved urls can be used e.g. local host
# {"access_token": "BQDMJOGNVLEnA0kutea1P6vY2EC5nk7JOuVEo4LVSzvnd5-mDR0LkywLCGmaMThTeGBKTOBBYR5tJPw5NrcyGB8ZWbVWMqWQV1pW58oKsAt6nQlF-ROxzzXPEHvZCTDHKBcUxxS1dGc7hehPOEsyuWu01IvfPKsyU5S6c7An1URb0faVyesRjrp9rbXTnmFwA9EbaqjmioUeNy_kXtCxDhEQosxsM_QnFA", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQAW3z1JNZ_-6k1wfqs4BGfJi4ZtzDxt_2AKk89gszoEpN2N6jObgfZPRbCXuYJX9RnvC1reE39TrjopRzhecUYbRnUygziPpJKuxfBqMR3TaCJPlPJ8DMciyRK3ZOoKzo4", "scope": "playlist-modify-private", "expires_at": 1665223435}

# Scopes
# user-read-currently-playing
# user-read-playback-position
# user-read-email
# user-top-read
# user-read-recently-played
# user-library-modify
# playlist-modify-private
# user-library-read

authentication_ongoing = True
while authentication_ongoing:
    # TODO Authenticate  and save the token file locally. Mine is saved inside the 'data' folder
    print("Authenticating Spotify request...")
    scope = "playlist-modify-private"  # Used to give write access to a user's private playlist
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                                   client_secret=spotify_client_secret,
                                                   redirect_uri=spotify_redirect_uri,
                                                   scope="playlist-modify-private",
                                                   show_dialog=True,
                                                   cache_path="data/token.txt"))

    # TODO Get the user id
    user_id = sp.current_user()["id"]
    if user_id != "":
        authentication_ongoing = False
        print(f"{user_id}")
        print("User ID retrieved")

# TODO Get the track URI
release_year = release_date_string.split("-")[0]
song_uris = []


# TODO Function to get the search results from Spotify. Empty searches will yield an empty list
def spotipy_request(track_name, release_year):
    response = sp.search(
        q=f"track:{track_name} year:{release_year}",
        type="track"
    )
    return response


# TODO Loop through the music titles list created after scraping the Billboard page and pass each of them and the release year as params
print("Searching for song titles on Spotify...")
search_results = []
for track_name in music_titles:
    try:
        response = spotipy_request(track_name, release_year)
        # print(response)
    except IndexError:
        pass
    else:
        search_results.append(response)

# TODO You can implement the same using threading. .submit will reorder the result which is not ideal. Use the map()
# with ThreadPoolExecutor(max_workers=100) as executor:
#     print("Searching for songs in spotify")
#     futures = [executor.submit(spotipy_request, track_name, release_year) for track_name in music_titles]
# for future in as_completed(futures):
#     result = future.result()
#     print(result)

# TODO Save the data locally for offline testing and verification
# with open(f"data/{release_date_string} spotify playlist.json", mode="w") as spotify_search_results_file:
#     json.dump(search_results, spotify_search_results_file, indent=4)

# TODO For offline testing
with open(f"data/{release_date_string} spotify playlist.json", mode="r") as spotify_charts_json_file:
    search_results = json.load(spotify_charts_json_file)

print("Confirming correct song and artist pair and obtaining the track uri...")
playlist = []
uri_list = []
for result in search_results:
    # TODO Get the track data
    track_data = result['tracks']['items']

    # TODO Get the index of the track result to compare its data with the Billboard data
    result_index = search_results.index(result)

    # TODO Eliminate tracks whose search results didn't bring back anything
    if len(track_data) != 0:

        # TODO Loop through the multiple search results for a single song
        for data in track_data:
            # TODO Get the artist name
            artist_name = data['artists'][0]['name']
            # print(data)

            # TODO Get the full billboard artist name corresponding to the index of the current track result and split to individual names and loop through each of them
            for billboard_name in artist_names[result_index].split(" "):
                track_name = data['name']
                # track_uri = data['artists'][0]['uri']
                track_uri = data['uri']

                # TODO Check if any of the separate artist individual names from the billboard match any that are from the spotify
                if any(billboard_name in spotify_name for spotify_name in artist_name.split(" ")):
                    # TODO Check if the name and the track have been added to the new playlist list
                    # This part of the code makes sure that an artist can have two entries in the list and two song
                    # with the same title from different artist can also appear
                    if not any(artist_name in track_dict["Artist Name"] for track_dict in playlist) and \
                            not any(artist_name in track_dict["Artist Name"] for track_dict in playlist):
                        # TODO Append the uri to a list
                        uri_list.append(track_uri)

                        # TODO Create a dict
                        track_dict = {}
                        track_dict["Artist Name"] = artist_name
                        track_dict["Track Name"] = track_name
                        track_dict["URI"] = track_uri

                        # print(track_dict)

                        # TODO Append the unique dict in the list
                        playlist.append(track_dict)

print(len(playlist), print(len(uri_list)))

# TODO Save the playlist offline
with open(f"data/{release_date_string} Billboard Top 100 playlist.json", mode="w") as playlist_file:
    json.dump(playlist, playlist_file, indent=4)


# TODO Create spotify playlist. Run this only once
print("Making the playlist")
playlist_feedback = sp.user_playlist_create(
    user=user_id,
    # name=f"{release_date_string} Billboard Top 100",
    name="Dituna, Welcome To The World",
    public=True,  # Make the playlist public or not
    description=f"{release_date_string} Billboard Top 100"
    # description="This playlist was created using python, Spotify api and spotipy library. To see the code, go to the link "
    #             "https://github.com/Vincent-Muchiri/Python-Programming and under the Python-Programming repository look for a folder named 'Billboards Top 100 Spotify Playlist Maker'"
            )

playlist_id = playlist_feedback['id']
# print(playlist_id)

# playlist_id = "Playlist ID"
# print(uri_list)

# TODO Upload songs to playlist
print("Adding the songs to the playlist")
playlist_snapshot = sp.playlist_add_items(
    playlist_id=playlist_id,
    items=uri_list,
)
print(
    f"Playlist Name: {release_date_string} Billboard Top 100\nPlaylist Snapshot ID: {playlist_snapshot['snapshot_id']}")
# Playlist Name: "1997-09-11 Billboard Top 100"
# Playlist Snapshot ID: "MyxiZTI2NWE5OTNiMDQxNjc4NTk4ZmE3NTVlYTRmZTNlZmNhYWE5MjNj"
