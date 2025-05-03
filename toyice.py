

import random
import requests
from PIL import Image
from base64 import b64encode
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import time
from urllib import *
import urllib
import json
import datetime

client_id = "e291792abd4b4a1db646f561c823beb9"
client_secret = "26e6df1ae3614825940739dd03c31feb"

auth_url = 'https://accounts.spotify.com/api/token'
auth_header = 'Basic ' + b64encode((client_id + ':' + client_secret).encode()).decode()

auth_data = {
    'grant_type': 'client_credentials'
}

auth_response = requests.post(auth_url, headers={'Authorization': auth_header}, data=auth_data)

if auth_response.status_code == 200:
    token = auth_response.json().get('access_token')
    #print('Token:', token)
else:
    print('Error:', auth_response.status_code)
    print(auth_response.text)
    
headers = {
    "Authorization": "Bearer " + token
}

def get_artists(genre, artist):
    genre = genre.lower()
    url = f"https://api.spotify.com/v1/search?q={artist}&type=artist"

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        artists_info = response.json()
        if artists_info["artists"]["items"] == []:
            print("No artists found for that genre!")
            return []
        else:
            for i in artists_info["artists"]["items"]:
                try:
                    if genre in i["genres"] and i["name"] == artist:
                        return i["id"]
                except IndexError:
                    print("Enter a valid genre or try a different artist!")
                    return []
    else:
        print("Enter a valid genre or try a different artist!")
        return []
    
def get_albums(genre, decade):
    lst = []
    albums_lst = []
    
    genre = genre.lower()
    
    if genre == "r&b":
        genre_adj = genre.replace("&", "%26")
    else:
        genre_adj = genre.replace(" ", "%20")
        
    decade = int(decade.strip("s"))

    if decade == 2020:
        start_year = 2020
        end_year = datetime.datetime.now().year
    else: 
        if decade < 2020:
          start_year = decade
          end_year = decade + 9
          
    offset = random.randint(0, 500)

    response = requests.get(f"https://api.spotify.com/v1/search?q=genre%3A%22{genre}%22%20year%3A{str(start_year)}-{str(end_year)}&type=track&limit=17&offset={offset}", headers=headers)

    if response.status_code == 200:

      tracks = response.json()

      tracks_found = tracks["tracks"]["items"]

      for album in tracks_found:
        if album["album"]["id"] not in lst:
          lst.append(album["album"]["id"])
          albums_lst += [[album["album"]["name"], album["album"]["artists"][0]["name"], album["album"]["release_date"]]]
        else:
          continue
      return albums_lst

API_KEY = "OdOTpaxGkQyamSaW2EkeanimV3vOKKdmyBTwQHGHxErCN97F3c1Z4kVR8UJWgM85"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def get_lyrics(artist):
    response = requests.get("https://api.genius.com/search", headers=HEADERS, params={"q": artist})
    data = response.json()

    if not data["response"]["hits"]:
        print("No songs found.\n")
        return []
    else:
        song = random.choice(data["response"]["hits"])["result"]
        
        title = song["title"]
        
        hint = song["title"][0]

        page = requests.get(song["url"])
        soup = BeautifulSoup(page.text, "html.parser")

        lyrics_divs = soup.find_all("div", class_=lambda x: x and "Lyrics__Container" in x)

        full_lyrics = ""
        
        for i in lyrics_divs:
            full_lyrics += i.text.strip()

        words = full_lyrics.split() 

        if len(words) >= 10:
            stop = random.randint(10, len(words))
            start = stop - 10
            consecutive_words = words[start:stop]
            song_lst = [title, " ".join(consecutive_words), hint]
            return song_lst
                
        else:
            print("Not enough words in the lyrics.\n")
            return []

def image(id):
    url = f"https://api.spotify.com/v1/artists/{id}"
    url_al = f"https://api.spotify.com/v1/artists/{id}/albums"
    response = requests.get(url, headers=headers)
    response_album = requests.get(url_al,headers=headers)
    
    if response.status_code != 200 or response_album.status_code != 200:
        print("Error fetching artist or album data.")
        return []
    
    data = response.json()
    name = data['name']
    alb_data = response_album.json()
    max = len(alb_data['items'])
    ran = random.randint(0,max-1)
    image_url = alb_data['items'][ran]['images'][0]['url']
    
    if max < 1:
        print('No album found')
        return []
    else:
        image_name = alb_data['items'][ran]['name']
        urllib.request.urlretrieve(image_url, f'{image_name}.jpg')
        img = Image.open(f'{image_name}.jpg')
        return [img, image_name]
    
def get_spotify_id(artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1  
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()
        if results["artists"]["items"]:
            artist = results["artists"]["items"][0]
            id = artist["id"]
            return id
        else:
            return "No artist found."
    else:
        return f"Error: {response.status_code} - {response.text}"
    
def main():
    print("Welcome to our spotify guessing game! You can guess albums in a certain genre, guess the song lyrics from a certain artist, or guess an album title from its cover.")
    response_1 = ""
    while True:
        response_1 = input("What would you like to do? Enter A to guess an album, enter B to guess a song title based on lyrics, or enter C to guess an album title from its cover.")
        if response_1.lower() == "a":
            score = 50
            
            response_4 = input("Enter a genre to guess an album from: ")
            response_15 = input("Enter a decade (Ex: 2020s): ")
            
            album_Q1 = get_albums(response_4, response_15)
            
            if album_Q1 == []:
                continue
  
            for i in range(0, len(album_Q1), 3):
                answers = []
                
                albums = album_Q1[i:i+3]
                
                if len(albums) < 3:
                    break
                
                answer_date = random.choice(albums)[2][0:4]
                
                for album in albums:
                    if album[2][0:4] == answer_date:
                        answers += [album[0]]
                        
                
                
                print(f"\nWhich album was released in {answer_date}\n")
                print(f"\n1. {albums[0][0]} - {albums[0][1]}\n2. {albums[1][0]} - {albums[1][1]}\n3. {albums[2][0]} - {albums[2][1]}\n")
        
                hint = list(answers[0])[0]

                response_6 = input(f"\nGuess the album from the list above: ")
                if response_6 in answers:
                    print(f"Correct! The album was {response_6}.")
                    
                else:
                    response_30 = input(f"\nIncorrect. Try Again: ")
                    if response_30 in answers:
                        print(f"Correct! The album was {response_30}.")
                    else: 
                        score -= 10
                        if len(answers) > 1:
                            print(f"Incorrect. The correct album was either {answers[0]} or {answers[1]}. Your score is {score}/50.\n")
                        else:
                            print(f"Incorrect. The correct album was {answers[0]}. Your score is {score}/50.\n")
            
            print(f"\nYour total score is {score}/50\n")
                
        elif response_1.lower() == "b":
            score = 0
            
            #question 1
            response_2 = input("Enter an artist's name: ")
            question_1 = get_lyrics(response_2)
            
            if question_1 == []:
                continue
            
            response_3 = input(f"Enter the song title for the following lyrics: {question_1[1]}\n")
            if response_3.lower() == question_1[0].lower():
                score += 10
                print(f"\nCorrect! Your score is {score}/30.\n")
            else:
                print(f"\nIncorrect. The correct answer was {question_1[0]}. Your current score is {score}/30\n")
            
            #question 2
            question_2 = get_lyrics(response_2)
            response_5 = input(f"Enter the song title for the following lyrics: {question_2[1]}\n")
            if response_5.lower() == question_2[0].lower():
                score += 10
                print(f"\nCorrect! Your score is {score}/30.\n")
            else:
                print(f"\nIncorrect. The correct answer was {question_2[0]}. Your current score is {score}/30\n")
            
            #question 3
            question_3 = get_lyrics(response_2)
            response_7 = input(f"Enter the song title for the following lyrics: {question_3[1]}\n")
            if response_7.lower() == question_3[0].lower():
                score += 10
                print(f"\nCorrect! Your score is {score}/30.\n")
            else:
                print(f"\nIncorrect. The correct answer was {question_3[0]}. Your current score is {score}/30\n")
            
            return f"Your score is {score}/30."
        
        elif response_1.lower() == "c":
            response_10 = input("Enter an artist to guess the title of their album based on the cover: ")
            spotify_id = get_spotify_id(response_10)
            
            if spotify_id == []:
                continue
            
            album_cover = image(spotify_id)
            hint = album_cover[1][0]
            album_cover[0].show()
            response_11 = input("Guess the album title: ")
            if response_11.lower() == album_cover[1].lower():
                print(f"\nCorrect! The album was {album_cover[1]}")
            else:
                response_12 = input("Guess again: ")
                print(f"The album begins with {hint}\n")
                
                if response_12.lower() == album_cover[1].lower():
                    return f"\nCorrect! The album was {album_cover[1]}"
                else:
                    response_13 = input("Guess one more time: ")
                    if response_13.lower() == album_cover[1].lower():
                        return f"\nCorrect! The album was {album_cover[1]}"
                    else:
                        return f"\nIncorrect. The album was {album_cover[1]}"
        else:
            print("Enter a letter from the option given\n")
            print(response_1)

main()