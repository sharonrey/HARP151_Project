import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import requests
import json
from base64 import b64encode
from bs4 import BeautifulSoup
import re
import spotipy
import datetime
import matplotlib.pyplot as plt
from urllib import *
import urllib
from io import BytesIO


client_id = "e291792abd4b4a1db646f561c823beb9"
client_secret = "26e6df1ae3614825940739dd03c31feb"

auth_url = 'https://accounts.spotify.com/api/token'
auth_header = 'Basic ' + b64encode((client_id + ':' + client_secret).encode()).decode()
url = "https://api.spotify.com/v1/search"

auth_data = {
    'grant_type': 'client_credentials'
}

auth_response = requests.post(auth_url, headers={'Authorization': auth_header}, data=auth_data)

if auth_response.status_code == 200:
    token = auth_response.json().get('access_token')
    print('Token:', token)
else:
    print('Error:', auth_response.status_code)
    print(auth_response.text)

token = "BQDLS51gIeE-tdAjx3S78yTN_8nus2WYiwXYS_tQE6ktSSIp2A-DaB8pwY-7Gm6iRnXOfkfGM3LmkB6LU-j07Vm3TRvAYmUUgVdAie09YVmUqwqrUtevOQAfvuBkF74RJQGnnECTNbs"

client_id = "fe26696907e44c8393d68a7f04883f8c"
client_secret = "eb52c38e47504474adee24d6232b24db"

auth_url = 'https://accounts.spotify.com/api/token'
auth_header = 'Basic ' + b64encode((client_id + ':' + client_secret).encode()).decode()

auth_data = {
    'grant_type': 'client_credentials'
}

#we are POSTING something to the server in order to RETURN the token
auth_response = requests.post(auth_url, headers={'Authorization': auth_header}, data=auth_data)

if auth_response.status_code == 200:
    token = auth_response.json().get('access_token')
    ###print('Token:', token)
else:
    print('Error:', auth_response.status_code)
    print(auth_response.text)

rap = [
    "Drake", "Kendrick Lamar", "Travis Scott", "Post Malone", "Eminem",
    "Kanye West", "Future", "Playboi Carti", "Doja Cat", "Pitbull",
    "Lil Nas X", "21 Savage", "Lil Baby", "Tyler, The Creator", "Juice WRLD",
    "Megan Thee Stallion", "Nicki Minaj", "Roddy Ricch", "Jack Harlow", "Cordae"]
latin = [
    "Bad Bunny", "J Balvin", "Shakira", "Karol G", "Daddy Yankee",
    "Anuel AA", "Maluma", "Ozuna", "Becky G", "Natti Natasha"]
rnb = [
    "The Weeknd", "SZA", "Rihanna", "Chris Brown", "Beyonc�",
    "Alicia Keys", "Giveon", "Brent Faiyaz", "Summer Walker"]
electronic = [
    "David Guetta", "Calvin Harris", "Marshmello", "Alan Walker", "Kygo",
    "Zedd", "Avicii", "The Chainsmokers", "Diplo"]
pop = [
    "Bruno Mars", "Lady Gaga", "Taylor Swift", "Ariana Grande",
    "Dua Lipa", "Ed Sheeran", "Justin Bieber", "Katy Perry", "Sabrina Carpenter",
    "Sia", "Selena Gomez", "Tate McRae", "Gracie Abrams", "Miley Cyrus",
    "Sam Smith", "Teddy Swims", "Maroon 5", "OneRepublic",
     "Shawn Mendes", "Camila Cabello", "Michael Jackson", "Lauv",
     "Zara Larsson", "Troye Sivan", "Conan Gray", "Charlie Puth","Harry Styles"]
indierock = [
    "Coldplay", "Imagine Dragons", "Arctic Monkeys", "Queen", "Lana Del Rey",
    "The Killers", "Red Hot Chili Peppers", "Foo Fighters", "Paramore", "Green Day"]

country = ["Morgan Wallen","Luke Combs", "Zach Bryan","Carrie Underwood","Shaboozey","Alan Jackson"
           ,"Tim Mcgraw","Kenny Chesney","Reba McEntire"]


headers = {
    "Authorization": "Bearer " + token
}

def raise_frame(frame):
    frame.tkraise()

def level_one():
    game_frame.pack_forget()
    level1_frame.pack(fill="both", expand=True)

def level_two():
    game_frame.pack_forget()
    level2frame.pack(fill="both", expand=True)

def level_three():
    game_frame.pack_forget()
    level3_frame.pack(fill="both", expand=True)

def return_game1():
    selection_frame.pack_forget()
    level1_frame.pack_forget()
    level1Qs_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)

def return_game2():
    level2frame.pack_forget()
    game_frame.pack(fill="both", expand=True)

def return_game3():
    level3_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    last_page.pack_forget()


root = tk.Tk()
root.title("Spotify Guessing Game")
root.geometry("610x760")
root.config(bg="#67D771", cursor="heart")

# Frames
game_frame = tk.Frame(root, bg="#67D771")
level1_frame = tk.Frame(root, bg="#67D771")
level1Qs_frame = tk.Frame(root, bg="#67D771")
level3_frame = tk.Frame(root, bg="#67D771")
level2frame = tk.Frame(root, bg="#67D771")
game_frame.pack(fill="both", expand=True)

toyice_path = "/Users/toyice/Documents/GitHub/HARP151_Project/spotify.jpg"
talia_path = "/Users/taliafante/Documents/harp 151/GitHub/HARP151_Project/spotify.jpg"
sharon_path = "/Users/sharonreynolds/Desktop/HARP151/HARP151_Project/spotify.jpg"
image = Image.open(toyice_path)
photo = ImageTk.PhotoImage(image, master=root)

# Intro
intro_canvas = tk.Canvas(game_frame, width=image.width, height=image.height, bg="#67D771", highlightthickness=0)
intro_canvas.create_image(115, 115, anchor="center", image=photo)
intro_canvas.image = photo
intro_canvas.pack(pady=20)

tk.Label(game_frame, text="Welcome to our Spotify Guessing Game!", font=("Helvetica", 22, "bold"), bg="#67D771").pack(pady=(10, 20))

tk.Label(game_frame, text="There are three levels to this game, and you have the option to choose \nbetween any of them!! You will be given 5 questions in each level and scored \nout of 50 points (each question counts for 10 points).\nPlease select from the options below!!", font=("Helvetica", 15), bg="#67D771", justify="center").pack(pady=(0, 20))

tk.Label(game_frame, text="Level 1: Guess the which album was released in a specific year with\nwith multiple choice questions (choose genre & decade)", font=("Helvetica", 14, "bold"), bg="#67D771").pack(pady=5)
tk.Label(game_frame, text="Level 2: Guess the song based on 10 lyrics words", font=("Helvetica", 14, "bold"), bg="#67D771").pack(pady=5)
tk.Label(game_frame, text="Level 3: Guess the name of an album from the cover photo with multiple choice\n questions (choose genre)", font=("Helvetica", 14, "bold"), bg="#67D771").pack(pady=5)

tk.Label(game_frame, text="Score: 50 points", font=("Helvetica", 13, "italic"), bg="#67D771").pack(pady=30)

button_frame = tk.Frame(game_frame, bg="#67D771")
button_frame.pack(pady=10)

# Levels
tk.Button(button_frame, text="Level 1", font=("Helvetica", 12), command=level_one, bg="white", width=12, height=2).grid(row=0, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Level 2", font=("Helvetica", 12), command=level_two, bg="white", width=12, height=2).grid(row=0, column=1, padx=10, pady=5)
tk.Button(button_frame, text="Level 3", font=("Helvetica", 12), command=level_three, bg="white", width=12, height=2).grid(row=0, column=2, padx=10, pady=5)

# Level 1
toyice_path2 = "/Users/toyice/Documents/GitHub/HARP151_Project/level1.jpg"
talia_path2 = "/Users/taliafante/Documents/harp 151/GitHub/HARP151_Project/level1.jpg"
# sharon_path = ""
image = Image.open(toyice_path2)
photo = ImageTk.PhotoImage(image, master=root)

# Intro
intro_canvas = tk.Canvas(level1_frame, width=image.width, height=image.height, bg="#67D771", highlightthickness=0)
intro_canvas.create_image(145, 100, anchor="center", image=photo)
intro_canvas.image = photo
intro_canvas.pack(pady=10)

album_lst = None

def start_game1():
    global album_lst
    selected_genre = value_genre.get()
    selected_decade = value_decade.get()
    if selected_genre == "Select a genre" or selected_decade == "Select a decade":
        messagebox.showwarning("Selection Missing", "Please select both a genre and a decade!")
    else:
        album_lst = get_albums(selected_genre, selected_decade)
        selection_frame.pack_forget()
        level1_frame.pack_forget()
        game1(album_lst)

tk.Label(level1_frame, text="<� Welcome to the Level 1: An album guessing game! <�\n\nSelect your genre and decade of choice to get \nquestions about random artists!!", font=("Helvetica", 18, "bold"), bg="#67D771").pack(pady=(20, 15))

selection_frame = tk.Frame(level1_frame, bg="#67D771")
selection_frame.pack(pady=10)

# Genre Selection
genre_list = ["Country", "Pop", "Rap", "Jazz", "Hip Hop", "Indie Rock", "Latin", "R&B"]
value_genre = tk.StringVar(value="Select a genre")

genre_menu = tk.OptionMenu(selection_frame, value_genre, *genre_list)
genre_menu.config(bg="white", fg="black", font=("Helvetica", 12), bd=2, width=15)
genre_menu.grid(row=0, column=0, padx=10, pady=10)

# Decade Selection
decade_list = ["1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"]
value_decade = tk.StringVar(value="Select a decade")

decade_menu = tk.OptionMenu(selection_frame, value_decade, *decade_list)
decade_menu.config(bg="white", fg="black", font=("Helvetica", 12), bd=2, width=15)
decade_menu.grid(row=0, column=1, padx=10, pady=10)

start1_button = tk.Button(level1_frame, text="Start Round", font=("Helvetica", 12), bg="white", command=start_game1, width=20, height=2).pack(pady=(20, 10))
return_button = tk.Button(level1_frame, text="Back to Game Intro", font=("Helvetica", 12), command=return_game1, bg="white", width=20, height=2).pack(pady=(5, 20))

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

level1_score = 50

def game1(album_lst):

    # if len(album_lst) < 3:
    #     for widget in level1Qs_frame.winfo_children():
    #         widget.destroy()
    #     return_game1()
    #     return

    count = 0
    answers = []

    album_names = []

    albums = []

    for i in range(0, len(album_lst)):
        if count == 3:
            break
        else:
            albums.append(album_lst[i])
            album_names += [f"{album_lst[i][0]} - {album_lst[i][1]}"]
            count += 1
            album_lst.pop(i)

    answer_date = random.choice(albums)[2][0:4]

    for album in albums:
        if album[2][0:4] == answer_date:
            answers += [f"{album[0]} - {album[1]}"]

    album1 = f"1. {album_names[0]}"
    album2 = f"2. {album_names[1]}"
    album3 = f"3. {album_names[2]}"

    album1_label = tk.Label(level1Qs_frame, text= album1, bg="#67D771",font=("Helvetica",15),foreground='black').pack()
    album2_label = tk.Label(level1Qs_frame, text= album2, bg="#67D771",font=("Helvetica",15),foreground='black').pack()
    album3_label = tk.Label(level1Qs_frame, text= album3, bg="#67D771",font=("Helvetica",15),foreground='black').pack()

    question = f"Which album was released in {answer_date}?"
    quesiton_label = tk.Label(level1Qs_frame,text= question, bg="#67D771",font=("Helvetica",15),foreground='black').pack(pady=20)


    def chosen_option():
        global level1_score
        choice = answer.get()
        select = ""

        if choice in answers:
            select = "Correct"
            add_score(scores)
        else :
            level1_score -= 10
            if len(answers) == 2:
                select = f"Wrong. The answer is either {answers[0]} or {answers[1]}"
            elif len(answers) == 1:
                select = f"Wrong. The answer is {answers[0]}"
            elif len(answers) == 3:
                select = f"Wrong. The answer is either {answers[0]} or {answers[1]} or {answers[2]}"

        result_label = tk.Label(level1Qs_frame, text=f"{choice} is {select}!", bg="#67D771",font=("Helvetica",15))
        result_label.pack(pady=20)
        choose_btn.forget()
        dropdown.forget()


        answer.set("Select an album")

        return choice

    #set() est's the initial value
    answer = tk.StringVar()
    answer.set("Pick an Album")

    #dropdownmenu syntax, tie it to a tkinter variable and a list
    dropdown = tk.OptionMenu(level1Qs_frame, answer, *album_names)

    choose_btn = tk.Button(level1Qs_frame, text="Click to Submit", command=chosen_option, width=10, height=2, bg="#67D771")
    dropdown.pack(pady=20)
    choose_btn.pack(pady=10)

    button_change = tk.Button(level1Qs_frame,text="Next Question",command= change_tabl1, width=10, height=2, bg="#67D771")
    button_change.pack(pady=10)
    level1Qs_frame.pack(pady=20)

def change_tabl1():
    if len(album_lst) < 3:
        messagebox.showinfo("Score", f"Your score is {level1_score}")
        return_game1()
        return
    
    for widget in level1Qs_frame.winfo_children():
        widget.destroy()

    level1Qs_frame.pack_forget()
    level1Qs_frame.pack(pady=20)

    game1(album_lst)

# Level 2
toyice_path3 = "/Users/toyice/Documents/GitHub/HARP151_Project/level2.jpg"
talia_path2 = "/Users/taliafante/Documents/harp 151/GitHub/HARP151_Project/level2.jpg"
# sharon_path = ""
image = Image.open(toyice_path3)
photo = ImageTk.PhotoImage(image, master=root)

# Intro
intro_canvas = tk.Canvas(level2frame, width=image.width, height=image.height, bg="#67D771", highlightthickness=0)
intro_canvas.create_image(145, 100, anchor="center", image=photo)
intro_canvas.image = photo
intro_canvas.pack(pady=10)

tk.Label(level2frame, text= "<� Welcome to the Level 2: A lyric guessing game! <�\n\n", font=("Helvetica", 18, "bold"), justify= "center", bg="#67D771").pack()

tk.Label(level2frame, text=   "You will be given a snippet of lyrics from songs by your chosen artist.\n"
            "- You start with 50 points.\n"
            "- If you guess wrong, you lose 5 points and receive a hint.\n"
            "- Guess wrong again or skip to the next question, you lose another 5 points.\n"
            "- The game ends after 5 questions.\n\n""", font=("Helvetica", 14, "bold"), justify= "left", bg="#67D771").pack(pady=5)


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

API_KEY = "OdOTpaxGkQyamSaW2EkeanimV3vOKKdmyBTwQHGHxErCN97F3c1Z4kVR8UJWgM85"
HEADERS = {"Authorization": f"Bearer {API_KEY}"} # did this in the coding center !!


selection_frame2 = tk.Frame(level2frame, bg="#67D771")
selection_frame2.pack(pady=10)

attempts = 0
points = 50
question_num = 0
max_questions = 5
used_lyrics = []
current_answer = ""
lyrics_label = None
entry = None
feedback_label = None
question_label = None
next_button = None
back_button = None


def start_game2():
    for widget in level2frame.winfo_children():
        widget.pack_forget()

    welcome_label = tk.Label(
        level2frame,
        text=("Type in an artists first and last name to begin!"), font=("Helvetica", 14), wraplength=550, justify="left", bg="#67D771")
    welcome_label.pack(pady=20)

    artist_label.pack(pady=10)
    artist_entry.pack(pady=5)
    artist_button.pack(pady=10)


def show_artist_input():
    for widget in level2frame.winfo_children():
        widget.pack_forget()

    artist_label.pack(pady=10)
    artist_entry.pack(pady=5)
    artist_button.pack(pady=10)

def get_lyrics_tk(artist):
    global back_button

    response = requests.get("https://api.genius.com/search", headers=HEADERS, params={"q": artist})
    data = response.json()

    if not data["response"]["hits"]:
        for widget in level2frame.winfo_children():
            widget.pack_forget()

        no_artist_label = tk.Label(level2frame, text="Artist not found. Please try again.", font=("Helvetica", 14), bg="#67D771")
        no_artist_label.pack(pady=10)

        back_button = tk.Button(level2frame, text="Back", font=("Helvetica", 14, "bold"), bg="white", command=show_artist_input, width=10, height=2)
        back_button.pack(pady=10)
        return None

    else:
        song = random.choice(data["response"]["hits"])["result"]
        title = song["title"]
        hint = song["title"][0]

        page = requests.get(song["url"])
        soup = BeautifulSoup(page.text, "html.parser")

        api_lyrics = soup.find_all("div", class_=lambda x: x and "Lyrics__Container" in x)

        individual_lyrics = []
        for div in api_lyrics:
            for string in div.stripped_strings:
                if not re.match(r'^\[.*\]$', string):
                    individual_lyrics.append(string)

        full_lyrics = " ".join(individual_lyrics)
        words = full_lyrics.split()

        if len(words) >= 10:
            stop = random.randint(10, len(words))
            start = stop - 10
            return [title, " ".join(words[start:stop]), hint]

        else:
            for widget in level2frame.winfo_children():
                widget.pack_forget()

            no_lyrics_label = tk.Label(level2frame, text="Not enough lyrics. Please try a different artist.", font=("Helvetica", 14), bg="#67D771")
            no_lyrics_label.pack(pady=10)

            back_button = tk.Button(level2frame, text="Back", font=("Helvetica", 14, "bold"), bg="white", command=show_artist_input)
            back_button.pack(pady=10)
            return None


def game2(artist):
    global question_num, used_lyrics, lyrics_label, entry, feedback_label, question_label, next_button, submit_button
    question_num = 0
    used_lyrics = []

    for widget in level2frame.winfo_children():
        widget.pack_forget()

    question_label = tk.Label(level2frame, text="", font=("Helvetica", 14, "bold"), bg="#67D771")
    lyrics_label = tk.Label(level2frame, text="", wraplength=500, bg="#67D771")
    entry = tk.Entry(level2frame, font=("Helvetica", 14, "bold"), bg="#67D771", bd=5)
    submit_button = tk.Button(level2frame, text="Submit", font=("Helvetica", 14, "bold"), bg="white", command=submit_answer, width=10, height=2)
    feedback_label = tk.Label(level2frame, text="", font=("Helvetica", 14, "bold"), bg="#67D771")
    next_button = tk.Button(level2frame, text="Next Question", font=("Helvetica", 14, "bold"), bg="white", command=lambda: next_question(artist), width=10, height=2)

    question_label.pack()
    lyrics_label.pack()
    entry.pack()
    submit_button.pack()
    feedback_label.pack()
    next_button.pack()

    next_button.config(state="disabled")

    next_question(artist)

def next_question(artist):
    global question_num, current_answer, used_lyrics, attempts, points

    if attempts == 1:
        points -= 5
        feedback_label.config(text=f"You skipped the second attempt. -5 points.\nCorrect answer was: {current_answer}", fg="red")

    attempts = 0

    if question_num >= max_questions:
        question_label.config(text=f"Game Over! Final Score: {points} points")
        lyrics_label.config(text="")
        entry.pack_forget()
        next_button.pack_forget()
        submit_button.pack_forget()
        feedback_label.config(text="")
        return

    while True:
        lyrics = get_lyrics_tk(artist)
        if lyrics is None:
            feedback_label.config(text="Couldn't get lyrics. Try again.")
            return
        if lyrics not in used_lyrics:
            break

    used_lyrics.append(lyrics)
    current_answer = lyrics[0]
    question_num += 1

    question_label.config(text=f"Question {question_num}/{max_questions}: Guess the song")
    lyrics_label.config(text=f"{lyrics[1]}")
    feedback_label.config(text="")
    entry.delete(0, tk.END)

def submit_answer():
    global attempts, points

    guess = entry.get().strip()
    if guess.lower() == current_answer.lower():
        feedback_label.config(text=f"Correct! You have {points} points.", fg="#296218")
        next_button.config(state="normal")
    else:
        attempts += 1
        points -= 5
        if attempts == 1:
            feedback_label.config(
                text=f"Incorrect. Hint: The song starts with '{current_answer[0]}'. Try again. (-5 points)",
                fg="#EC5B2A"
            )
        elif attempts == 2:
            feedback_label.config(
                text=f"Incorrect again. The correct answer was: {current_answer}. (-5 more points)",
                fg="red"
            )
            next_button.config(state="normal")

artist_button = tk.Button(level2frame, text="Submit", font=("Helvetica", 14, "bold"), bg="white",
                          command=lambda: game2(artist_string.get()), width=10, height=2
                          )

artist_string = tk.StringVar()
artist_entry = tk.Entry(level2frame, textvariable=artist_string, font=("Helvetica", 14), bg="white", bd=5)
artist_label = tk.Label(level2frame, text="Enter artist name:", font=("Helvetica", 14, "bold"), bg="#67D771")



# Level 3
toyice_path4 ="/Users/toyice/Documents/GitHub/HARP151_Project/level3.jpg"
talia_path2 = "/Users/taliafante/Documents/harp 151/GitHub/HARP151_Project/level3.jpg"
# sharon_path = ""
image = Image.open(toyice_path4)
photo = ImageTk.PhotoImage(image, master=root)

# Intro
intro_canvas = tk.Canvas(level3_frame, width=image.width, height=image.height, bg="#67D771", highlightthickness=0)
intro_canvas.create_image(145, 100, anchor="center", image=photo)
intro_canvas.image = photo
intro_canvas.pack(pady=10)

tk.Label(level3_frame, text="<� Welcome to the Level 3: A album cover guessing game! <�\n\nSelect your genre of choice to get \npictures of random album covers!!", font=("Helvetica", 18, "bold"), bg="#67D771").pack(pady=(20, 15))


genres = ["Rap",'Electronic','Pop','Indie Rock','Latin','R&B','Country']
selected_genre = tk.StringVar()
selected_decade = tk.StringVar()

scores = 0

def add_score(score):
    score += 10
    return score

q1 = tk.Frame(root)
q1.configure(bg = "#67D771")
q2 = tk.Frame(root)
q2.configure(bg = "#67D771")
q3 = tk.Frame(root)
q3.configure(bg = "#67D771")
q4 = tk.Frame(root)
q4.configure(bg = "#67D771")
q5 = tk.Frame(root)
q5.configure(bg = "#67D771")

last_page = tk.Frame(root)
last_page.configure(bg = "#67D771")
point = []

def change_tab1():
    level3_frame.forget()
    q2.tkraise()
    flick2()
    root.update_idletasks()


def change_tab2():
    q2.forget()
    q3.tkraise()
    flick3()
    root.update_idletasks()


def change_tab3():
    q3.forget()
    q4.tkraise()
    flick4()
    root.update_idletasks()


def change_tab4():
    q4.forget()
    q5.tkraise()
    flick5()
    root.update_idletasks()

def last():
    q5.forget()
    last_page.tkraise()
    last_page.pack()
    root.update_idletasks()

genre_menu = tk.OptionMenu(level3_frame, selected_genre, *genres)
genre_menu.configure(font=("Helvetica",12),bg='#67D771')

selected_genre.set('Select genre')

def get_artist(genre):
    if genre == "pop" :
        x = random.choice(pop)
    elif genre == "indierock":
        x = random.choice(indierock)
    elif genre == "electronic" :
        x = random.choice(electronic)
    elif genre == "rap" :
        x = random.choice(rap)
    elif genre == "latin" :
        x = random.choice(latin)
    elif genre == "rnb" :
        x = random.choice(rnb)
    elif genre == "country" :
        x = random.choice(country)
    return x


def start_game():
    genre_menu.pack(pady=10)


def return_game4():
    last_page.forget()
    game_frame.pack()

def flick1():

        artist = get_artist(selected_genre.get())

        nameofart = f"https://api.spotify.com/v1/search?q={artist}&type=artist"

        name_res = requests.get(nameofart,headers=headers)
        name_data = name_res.json()
        #print(name_data['artists']['items'][0]['id'])

        id = name_data['artists']['items'][0]['id']

        url = f"https://api.spotify.com/v1/artists/{id}"
        url_al = f"https://api.spotify.com/v1/artists/{id}/albums"
        response = requests.get(url, headers=headers)
        response_album = requests.get(url_al,headers=headers)
        data = response.json()
        alb_data = response_album.json()
        #print(alb_data)
        #print(alb_data['items'][0]['images'][0]['url'])
        #print(search_data)
        #name = data['name']
        max = len(alb_data['items'])
        #artist_id = data['id']
        #sets up a global variable for name and id


        answer_list = []

        al_list = []
        for ww in range(max):
            #print(alb_data['items'][ww]['name'])
            #print(alb_data['items'][ww]['name'])
            if alb_data['items'][ww]['album_type'] == 'album' :
                al_list.append(alb_data['items'][ww]['name'])
        #print(al_list)

        def answers():
            if len(al_list) >= 3 :
                random_answer = random.sample(al_list,3)
                for i in range(3) :
                    answer_list.append(random_answer[i])
            else :
                random_answer = random.sample(al_list,len(al_list))
                for z in range(len(random_answer)) :
                    answer_list.append(random_answer[z])
            print(answer_list)


        #ran = random.randint(0,max-1)
        #image_url = alb_data['items'][ran]['images'][0]['url']
        #image_name = alb_data['items'][ran]['name']
        #answer_list.append(image_name)
        answers()
        b = 0
        while True :
            if alb_data['items'][b]['name'] not in answer_list and alb_data['items'][b]['album_type'] == 'album' :
                image_url = alb_data['items'][b]['images'][0]['url']
                image_name = alb_data['items'][b]['name']
                answer_list.append(image_name)
                break
            elif b == len(alb_data['items']) :
                image_url = alb_data['items'][b]['images'][0]['url']
                break
            else :
                b +=1


        print(answer_list)

        def daname():
            return(image_name)




        def image():
            return(image_url)


        def load_image(img_url):
            try:
                response = requests.get(img_url)
                image_info = BytesIO(response.content) #content is an attribute that contains bytes; BytesIO transforms bytes into an object Pillow can open
                pil_img = Image.open(image_info).resize((300, 300))
                return ImageTk.PhotoImage(pil_img)
            except:
                print("not working")
                return None

        def display_image(url):
            global img_reference #to prevent Python from deleting this from memory before Tkinter can show it, ie. "garbage collected"
            pillow_img = load_image(url)
            if pillow_img is not None:
                canvas.delete("all")
                canvas.create_image(150, 150, anchor="center", image=pillow_img) #anchors image center at the 150,150 coordinate, or at the center of our 300x300 canvas
                img_reference = pillow_img

        canvas = tk.Canvas(level3_frame, width=300, height=300, bg="black", relief="solid")
        canvas.pack()

        #print(data)

        display_image(image())



        random_answer2 = random.sample(answer_list,len(answer_list))


        #for o in range(4):
        #    answer_list2.append(random_answer2[o])


        # canvas work
        question = 'What album is this ?'
        quesiton_label = tk.Label(level3_frame,text= question, bg="#67D771",font=("Helvetica",15),foreground='black').pack()


        def chosen_option():
            global score
            choice = answer.get()
            select = ""

            if choice == answer_list[len(answer_list ) -1] :
                select = "Correct"
                add_score(scores)
            else :
                select ="Wrong"

            result_label = tk.Label(level3_frame, text=f"{choice} is {select}!")
            result_label.pack()
            choose_btn.forget()
            dropdown.forget()


            answer.set("Select a album")

            return choice

        #set() est's the initial value
        answer = tk.StringVar()
        answer.set("Pick an Album ")

        #dropdownmenu syntax, tie it to a tkinter variable and a list
        dropdown = tk.OptionMenu(level3_frame, answer, *random_answer2)

        choose_btn = tk.Button(level3_frame, text="Click to submit", command=chosen_option, width=10, height=2, bg="#67D771")
        dropdown.pack()
        choose_btn.pack()

        button_change = tk.Button(level3_frame,text="Next question",command= change_tab1, width=10, height=2, bg="#67D771")
        button_change.pack()
        level3_frame.pack()


def flick2():
        artist = get_artist(selected_genre.get())

        nameofart = f"https://api.spotify.com/v1/search?q={artist}&type=artist"

        name_res = requests.get(nameofart,headers=headers)
        name_data = name_res.json()
        #print(name_data['artists']['items'][0]['id'])

        id = name_data['artists']['items'][0]['id']

        url = f"https://api.spotify.com/v1/artists/{id}"
        url_al = f"https://api.spotify.com/v1/artists/{id}/albums"
        response = requests.get(url, headers=headers)
        response_album = requests.get(url_al,headers=headers)
        data = response.json()
        alb_data = response_album.json()
        #print(alb_data)
        #print(alb_data['items'][0]['images'][0]['url'])
        #print(search_data)
        #name = data['name']
        max = len(alb_data['items'])
        artist_id = data['id']
        #sets up a global variable for name and id


        answer_list = []

        al_list = []
        for ww in range(max):
            #print(alb_data['items'][ww]['name'])
            #print(alb_data['items'][ww]['name'])
            if alb_data['items'][ww]['album_type'] == 'album' :
                al_list.append(alb_data['items'][ww]['name'])
        #print(al_list)

        def answers():
            if len(al_list) >= 3 :
                random_answer = random.sample(al_list,3)
                for i in range(3) :
                    answer_list.append(random_answer[i])
            else :
                random_answer = random.sample(al_list,len(al_list))
                for z in range(len(random_answer)) :
                    answer_list.append(random_answer[z])

            print(answer_list)



        #ran = random.randint(0,max-1)
        #image_url = alb_data['items'][ran]['images'][0]['url']
        #image_name = alb_data['items'][ran]['name']
        #answer_list.append(image_name)
        answers()
        b = 0
        while True :
            if alb_data['items'][b]['name'] not in answer_list and alb_data['items'][b]['album_type'] == 'album' :
                image_url = alb_data['items'][b]['images'][0]['url']
                image_name = alb_data['items'][b]['name']
                answer_list.append(image_name)
                break
            elif b == len(alb_data['items']) :
                image_url = alb_data['items'][b]['images'][0]['url']
                break
            else :
                b +=1

        print(answer_list)

        def daname():
            return(image_name)




        def image():
            return(image_url)
            #print(answer_list)
            #print(h(country))
            #print(image_name)
            #print(data['name'])
            #print(image_name)
            #urllib.request.urlretrieve(image_url, f'{image_name}.jpg')
            #img = Image.open(f'{image_name}.jpg')
            #img.show()
        #shows the image and prints the name of album

        def load_image(img_url):
            try:
                response = requests.get(img_url)
                image_info = BytesIO(response.content) #content is an attribute that contains bytes; BytesIO transforms bytes into an object Pillow can open
                pil_img = Image.open(image_info).resize((300, 300))
                return ImageTk.PhotoImage(pil_img)
            except:
                print("not working")
                return None

        def display_image(url):
            global img_reference #to prevent Python from deleting this from memory before Tkinter can show it, ie. "garbage collected"
            pillow_img = load_image(url)
            if pillow_img is not None:
                canvas.delete("all")
                canvas.create_image(150, 150, anchor="center", image=pillow_img) #anchors image center at the 150,150 coordinate, or at the center of our 300x300 canvas
                img_reference = pillow_img

        canvas = tk.Canvas(q2, width=300, height=300, bg="black", relief="solid")
        canvas.pack()

        #print(data)

        display_image(image())



        random_answer2 = random.sample(answer_list,len(answer_list))


        #for o in range(4):
        #    answer_list2.append(random_answer2[o])


        # canvas work
        question = 'What album is this ?'
        quesiton_label = tk.Label(q2,text= question, bg="#67D771",font=("Helvetica",15),foreground='black').pack()


        def chosen_option():
            global score
            choice = answer.get()
            select = ""

            if choice == answer_list[len(answer_list ) -1] :
                select = "Correct"
                add_score(scores)
                if "10" in point :
                    point.append("20")
                else :
                    point.append("10")
            else :
                select ="Wrong"

            result_label = tk.Label(q2, text=f"{choice} is {select}!")
            result_label.pack()
            dropdown.forget()
            choose_btn.forget()

            answer.set("Select a album")

            return choice

        #set() est's the initial value
        answer = tk.StringVar()
        answer.set("Pick an Album ")

        #dropdownmenu syntax, tie it to a tkinter variable and a list
        dropdown = tk.OptionMenu(q2, answer, *random_answer2)
        choose_btn = tk.Button(q2, text="Click to submit", command=chosen_option, width=10, height=2, bg="#67D771")

        dropdown.pack()
        choose_btn.pack()


        button_change = tk.Button(q2,text="Next question",command=change_tab2, width=10, height=2, bg="#67D771")
        button_change.pack()
        q2.pack()


def flick3():
        artist = get_artist(selected_genre.get())

        nameofart = f"https://api.spotify.com/v1/search?q={artist}&type=artist"

        name_res = requests.get(nameofart,headers=headers)
        name_data = name_res.json()
        #print(name_data['artists']['items'][0]['id'])

        id = name_data['artists']['items'][0]['id']

        url = f"https://api.spotify.com/v1/artists/{id}"
        url_al = f"https://api.spotify.com/v1/artists/{id}/albums"
        response = requests.get(url, headers=headers)
        response_album = requests.get(url_al,headers=headers)
        data = response.json()
        alb_data = response_album.json()
        #print(alb_data)
        #print(alb_data['items'][0]['images'][0]['url'])
        #print(search_data)
        #name = data['name']
        max = len(alb_data['items'])
        artist_id = data['id']
        #sets up a global variable for name and id


        answer_list = []

        al_list = []
        for ww in range(max):
            #print(alb_data['items'][ww]['name'])
            #print(alb_data['items'][ww]['name'])
            if alb_data['items'][ww]['album_type'] == 'album' :
                al_list.append(alb_data['items'][ww]['name'])
        #print(al_list)

        def answers():
            if len(al_list) >= 3 :
                random_answer = random.sample(al_list,3)
                for i in range(3) :
                    answer_list.append(random_answer[i])
            else :
                random_answer = random.sample(al_list,len(al_list))
                for z in range(len(random_answer)) :
                    answer_list.append(random_answer[z])
            print(answer_list)


        #ran = random.randint(0,max-1)
        #image_url = alb_data['items'][ran]['images'][0]['url']
        #image_name = alb_data['items'][ran]['name']
        #answer_list.append(image_name)
        answers()
        b = 0
        while True :
            if alb_data['items'][b]['name'] not in answer_list and alb_data['items'][b]['album_type'] == 'album' :
                image_url = alb_data['items'][b]['images'][0]['url']
                image_name = alb_data['items'][b]['name']
                answer_list.append(image_name)
                break
            elif b == len(alb_data['items']) :
                image_url = alb_data['items'][b]['images'][0]['url']
                break
            else :
                b +=1

        print(answer_list)

        def daname():
            return(image_name)




        def image():
            return(image_url)
            #print(answer_list)
            #print(h(country))
            #print(image_name)
            #print(data['name'])
            #print(image_name)
            #urllib.request.urlretrieve(image_url, f'{image_name}.jpg')
            #img = Image.open(f'{image_name}.jpg')
            #img.show()
        #shows the image and prints the name of album

        def load_image(img_url):
            try:
                response = requests.get(img_url)
                image_info = BytesIO(response.content) #content is an attribute that contains bytes; BytesIO transforms bytes into an object Pillow can open
                pil_img = Image.open(image_info).resize((300, 300))
                return ImageTk.PhotoImage(pil_img)
            except:
                print("not working")
                return None

        def display_image(url):
            global img_reference #to prevent Python from deleting this from memory before Tkinter can show it, ie. "garbage collected"
            pillow_img = load_image(url)
            if pillow_img is not None:
                canvas.delete("all")
                canvas.create_image(150, 150, anchor="center", image=pillow_img) #anchors image center at the 150,150 coordinate, or at the center of our 300x300 canvas
                img_reference = pillow_img

        canvas = tk.Canvas(q3, width=300, height=300, bg="black", relief="solid")
        canvas.pack()

        #print(data)

        display_image(image())



        random_answer2 = random.sample(answer_list,len(answer_list))


        #for o in range(4):
        #    answer_list2.append(random_answer2[o])


        # canvas work
        question = 'What album is this ?'
        quesiton_label = tk.Label(q3,text= question, bg="#67D771",font=("Helvetica",15),foreground='black').pack()


        def chosen_option():
            global score
            choice = answer.get()
            select = ""

            if choice == answer_list[len(answer_list ) -1] :
                select = "Correct"
                add_score(scores)
                if "10" in point and "20" in point :
                    point.append("30")
                elif "10" in point :
                    point.append("20")
                else :
                    point.append("10")
            else :
                select ="Wrong"

            result_label = tk.Label(q3, text=f"{choice} is {select}!")
            result_label.pack()
            dropdown.forget()
            choose_btn.forget()
            answer.set("Select a album")

            return choice

        #set() est's the initial value
        answer = tk.StringVar()
        answer.set("Pick an Album ")

        #dropdownmenu syntax, tie it to a tkinter variable and a list
        dropdown = tk.OptionMenu(q3, answer, *random_answer2)
        choose_btn = tk.Button(q3, text="Click to submit", command=chosen_option, width=10, height=2, bg="#67D771")

        dropdown.pack()
        choose_btn.pack()

        button_change = tk.Button(q3,text="Next question",command=change_tab3, width=10, height=2, bg="#67D771")
        button_change.pack()
        q3.pack()


def flick4():
        artist = get_artist(selected_genre.get())

        nameofart = f"https://api.spotify.com/v1/search?q={artist}&type=artist"

        name_res = requests.get(nameofart,headers=headers)
        name_data = name_res.json()
        #print(name_data['artists']['items'][0]['id'])

        id = name_data['artists']['items'][0]['id']

        url = f"https://api.spotify.com/v1/artists/{id}"
        url_al = f"https://api.spotify.com/v1/artists/{id}/albums"
        response = requests.get(url, headers=headers)
        response_album = requests.get(url_al,headers=headers)
        data = response.json()
        alb_data = response_album.json()
        #print(alb_data)
        #print(alb_data['items'][0]['images'][0]['url'])
        #print(search_data)

        #name = data['name']
        max = len(alb_data['items'])
        artist_id = data['id']
        #sets up a global variable for name and id


        answer_list = []

        al_list = []
        for ww in range(max):
            #print(alb_data['items'][ww]['name'])
            #print(alb_data['items'][ww]['name'])
            if alb_data['items'][ww]['album_type'] == 'album' :
                al_list.append(alb_data['items'][ww]['name'])
        #print(al_list)

        def answers():
            if len(al_list) >= 3 :
                random_answer = random.sample(al_list,3)
                for i in range(3) :
                    answer_list.append(random_answer[i])
            else :
                random_answer = random.sample(al_list,len(al_list))
                for z in range(len(random_answer)) :
                    answer_list.append(random_answer[z])
            print(answer_list)


        #ran = random.randint(0,max-1)
        #image_url = alb_data['items'][ran]['images'][0]['url']
        #image_name = alb_data['items'][ran]['name']
        #answer_list.append(image_name)
        answers()
        b = 0
        while True :
            if alb_data['items'][b]['name'] not in answer_list and alb_data['items'][b]['album_type'] == 'album' :
                image_url = alb_data['items'][b]['images'][0]['url']
                image_name = alb_data['items'][b]['name']
                answer_list.append(image_name)
                break
            elif b == len(alb_data['items']) :
                image_url = alb_data['items'][b]['images'][0]['url']
                break
            else :
                b +=1

        print(answer_list)

        def daname():
            return(image_name)




        def image():
            return(image_url)
            #print(answer_list)
            #print(h(country))
            #print(image_name)
            #print(data['name'])
            #print(image_name)
            #urllib.request.urlretrieve(image_url, f'{image_name}.jpg')
            #img = Image.open(f'{image_name}.jpg')
            #img.show()
        #shows the image and prints the name of album

        def load_image(img_url):
            try:
                response = requests.get(img_url)
                image_info = BytesIO(response.content) #content is an attribute that contains bytes; BytesIO transforms bytes into an object Pillow can open
                pil_img = Image.open(image_info).resize((300, 300))
                return ImageTk.PhotoImage(pil_img)
            except:
                print("not working")
                return None

        def display_image(url):
            global img_reference #to prevent Python from deleting this from memory before Tkinter can show it, ie. "garbage collected"
            pillow_img = load_image(url)
            if pillow_img is not None:
                canvas.delete("all")
                canvas.create_image(150, 150, anchor="center", image=pillow_img) #anchors image center at the 150,150 coordinate, or at the center of our 300x300 canvas
                img_reference = pillow_img

        canvas = tk.Canvas(q4, width=300, height=300, bg="black", relief="solid")
        canvas.pack()

        #print(data)

        display_image(image())



        random_answer2 = random.sample(answer_list,len(answer_list))


        #for o in range(4):
        #    answer_list2.append(random_answer2[o])


        # canvas work
        question = 'What album is this ?'
        quesiton_label = tk.Label(q4,text= question, bg="#67D771",font=("Helvetica",15),foreground='black').pack()


        def chosen_option():
            global score
            choice = answer.get()
            select = ""

            if choice == answer_list[len(answer_list ) -1] :
                select = "Correct"
                add_score(scores)
                if "10" in point and "20" in point and "30" in point:
                    point.append("40")
                elif "10" in point and "20" in point :
                    point.append("30")
                elif "10" in point :
                    point.append("20")
                else :
                    point.append("10")


            else :
                select ="Wrong"

            result_label = tk.Label(q4, text=f"{choice} is {select}!")
            result_label.pack()
            dropdown.forget()
            choose_btn.forget()
            answer.set("Select a album")

            return choice

        #set() est's the initial value
        answer = tk.StringVar()
        answer.set("Pick an Album ")

        #dropdownmenu syntax, tie it to a tkinter variable and a list
        dropdown = tk.OptionMenu(q4, answer, *random_answer2)
        choose_btn = tk.Button(q4, text="Click to Submit", command=chosen_option, width=10, height=2, bg="#67D771")

        dropdown.pack()
        choose_btn.pack()

        button_change = tk.Button(q4,text="Next question",command=change_tab4, width=10, height=2, bg="#67D771")
        button_change.pack()
        q4.pack()

def flick5():
        artist = get_artist(selected_genre.get())

        nameofart = f"https://api.spotify.com/v1/search?q={artist}&type=artist"

        name_res = requests.get(nameofart,headers=headers)
        name_data = name_res.json()
        #print(name_data['artists']['items'][0]['id'])

        id = name_data['artists']['items'][0]['id']

        url = f"https://api.spotify.com/v1/artists/{id}"
        url_al = f"https://api.spotify.com/v1/artists/{id}/albums"
        response = requests.get(url, headers=headers)
        response_album = requests.get(url_al,headers=headers)
        data = response.json()
        alb_data = response_album.json()
        #print(alb_data)
        #print(alb_data['items'][0]['images'][0]['url'])
        #print(search_data)
        #name = data['name']
        max = len(alb_data['items'])
        artist_id = data['id']
        #sets up a global variable for name and id


        answer_list = []

        al_list = []
        for ww in range(max):
            #print(alb_data['items'][ww]['name'])
            #print(alb_data['items'][ww]['name'])
            if alb_data['items'][ww]['album_type'] == 'album' :
                al_list.append(alb_data['items'][ww]['name'])
        #print(al_list)

        def answers():
            if len(al_list) >= 3 :
                random_answer = random.sample(al_list,3)
                for i in range(3) :
                    answer_list.append(random_answer[i])
            else :
                random_answer = random.sample(al_list,len(al_list))
                for z in range(len(random_answer)) :
                    answer_list.append(random_answer[z])
            print(answer_list)



        #ran = random.randint(0,max-1)
        #image_url = alb_data['items'][ran]['images'][0]['url']
        #image_name = alb_data['items'][ran]['name']
        #answer_list.append(image_name)
        answers()
        b = 0
        while True :
            if alb_data['items'][b]['name'] not in answer_list and alb_data['items'][b]['album_type'] == 'album' :
                image_url = alb_data['items'][b]['images'][0]['url']
                image_name = alb_data['items'][b]['name']
                answer_list.append(image_name)
                break
            elif b == len(alb_data['items']) :
                image_url = alb_data['items'][b]['images'][0]['url']
                break
            else:
                b +=1

        print(answer_list)

        def daname():
            return(image_name)




        def image():
            return(image_url)
            #print(answer_list)
            #print(h(country))
            #print(image_name)
            #print(data['name'])
            #print(image_name)
            #urllib.request.urlretrieve(image_url, f'{image_name}.jpg')
            #img = Image.open(f'{image_name}.jpg')
            #img.show()
        #shows the image and prints the name of album

        def load_image(img_url):
            try:
                response = requests.get(img_url)
                image_info = BytesIO(response.content) #content is an attribute that contains bytes; BytesIO transforms bytes into an object Pillow can open
                pil_img = Image.open(image_info).resize((300, 300))
                return ImageTk.PhotoImage(pil_img)
            except:
                print("not working")
                return None

        def display_image(url):
            global img_reference #to prevent Python from deleting this from memory before Tkinter can show it, ie. "garbage collected"
            pillow_img = load_image(url)
            if pillow_img is not None:
                canvas.delete("all")
                canvas.create_image(150, 150, anchor="center", image=pillow_img) #anchors image center at the 150,150 coordinate, or at the center of our 300x300 canvas
                img_reference = pillow_img

        canvas = tk.Canvas(q5, width=300, height=300, bg="black", relief="solid")
        canvas.pack()

        #print(data)

        display_image(image())



        random_answer2 = random.sample(answer_list,len(answer_list))


        #for o in range(4):
        #    answer_list2.append(random_answer2[o])


        # canvas work
        question = 'What album is this ?'
        quesiton_label = tk.Label(q5,text= question, bg="#67D771",font=("Helvetica",15),foreground='black').pack()


        def chosen_option():
            global score
            choice = answer.get()
            select = ""

            if choice == answer_list[len(answer_list ) -1] :
                select = "Correct"
                add_score(scores)
                if "10" in point and "20" in point and "30" in point and "40" in point:
                    point.append("50")
                elif "10" in point and "20" in point and "30" in point :
                    point.append("40")
                elif "10" in point and "20" in point  :
                    point.append("30")
                elif "10" in point :
                    point.append("20")
                else:
                    point.append("10")
            else :
                select ="Wrong"


            result_label = tk.Label(q5, text=f"{choice} is {select}!")
            result_label.pack()
            dropdown.forget()
            choose_btn.forget()

            answer.set("Select a album")

            return choice , point

        #set() est's the initial value
        answer = tk.StringVar()
        answer.set("Pick an Album ")

        #dropdownmenu syntax, tie it to a tkinter variable and a list
        dropdown = tk.OptionMenu(q5, answer, *random_answer2)
        choose_btn = tk.Button(q5, text="Click to submit", command= chosen_option, width=10, height=2, bg="#67D771")
        dropdown.pack()
        choose_btn.pack()

        button_change = tk.Button(q5,text="Reveal your score", command= last, width=10, height=2, bg="#67D771")
        button_change.pack()
        q5.pack()


def start_game3():
    genre_menu.destroy()
    flick1()

def clear():
    final.destroy()
    tk.Button.destory()
    #excit.forget()


final = tk.Label(last_page,text = f"You scored {scores} out of 50 on the album guessing game",bg="#67D771",font=("Helvetica",17)).pack()
#excit = tk.Button(last_page,text=" Back To Homepage", command= lambda: return_game3,font=("Helvetica",20), bg="#67D771",foreground = "black").pack()

#start_button3 = tk.Button(level3_frame, text="Start Round", font=("Helvetica", 12), bg="white", command=start_game3, width=20, height=2).pack(pady=(20, 10))
tk.Button(last_page, text="Back to Game Intro", font=("Helvetica", 12), command= return_game3, bg="white", width=20, height=2).pack(pady=(5, 20))



    # UI Elements
#decade_menu = tk.OptionMenu(root, selected_decade, *decades.keys())
#selected_decade.set('2000s')


genre_menu.pack()
start_button3 = tk.Button(level3_frame, text="Start Round", font=("Helvetica", 12), bg="white", command=start_game3, width=20, height=2).pack(pady=(20, 10))
tk.Button(level3_frame, text="Back to Game Intro", font=("Helvetica", 12), command=return_game3, bg="white", width=20, height=2).pack(pady=(5, 20))

start_button2 = tk.Button(level2frame, text="Start Round", font=("Helvetica", 12), bg="white", command=start_game2, width=20, height=2).pack(pady=(20, 10))
tk.Button(level2frame, text="Back to Game Intro", font=("Helvetica", 12), command=return_game2, bg="white", width=20, height=2).pack(pady=(5, 20))

root.mainloop()

# %% [markdown]
# Sources:
# 
# Intro
# 
# 
# Level 1
# 
# 
# Level 2
# - winfo_children() - https://www.geeksforgeeks.org/how-to-clear-out-a-frame-in-the-tkinter/
# - label options - https://www.geeksforgeeks.org/python-tkinter-label/
# - re.match - https://docs.python.org/3/library/re.html#re.match 
# - lamba function- https://www.w3schools.com/python/python_lambda.asp 
# 
# Level3


