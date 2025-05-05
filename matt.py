#base 64 allows us to encode our string
import requests
from bs4 import BeautifulSoup 
import spotipy
import tkinter as tk
from PIL import Image, ImageTk
from base64 import b64encode
import matplotlib.pyplot as plt
import random
import time
from urllib import *
import urllib
from io import BytesIO

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
    "The Weeknd", "SZA", "Rihanna", "Chris Brown", "Beyoncé",
    "Alicia Keys", "H.E.R.", "Giveon", "Brent Faiyaz", "Summer Walker"], 
electronic = [
    "David Guetta", "Calvin Harris", "Marshmello", "Alan Walker", "Kygo",
    "Zedd", "Martin Garrix", "Avicii", "The Chainsmokers", "Diplo"]
pop = [
    "Bruno Mars", "Lady Gaga", "Billie Eilish", "Taylor Swift", "Ariana Grande",
    "Dua Lipa", "Ed Sheeran", "Justin Bieber", "Katy Perry", "Sabrina Carpenter",
    "Sia", "Selena Gomez", "Tate McRae", "Gracie Abrams", "Miley Cyrus",
    "Sam Smith", "Benson Boone", "Teddy Swims", "Maroon 5", "OneRepublic",
    "Olivia Rodrigo", "Shawn Mendes", "Camila Cabello", "Michael Jackson", "Lauv",
    "Ava Max", "Zara Larsson", "Troye Sivan", "Conan Gray", "Charlie Puth","Harry Styles"]
indierock = [
    "Coldplay", "Imagine Dragons", "Arctic Monkeys", "Queen", "Lana Del Rey",
    "The Killers", "Red Hot Chili Peppers", "Foo Fighters", "Paramore", "Green Day"] 

country = ["Morgan Wallen","Luke Combs", "Zach Bryan","Carrie Underwood","Shaboozey","Alan Jackson"
           ,"Tim Mcgraw","Kenny Chesney","Reba McEntire"]



headers = {
    "Authorization": "Bearer " + token
}

root = tk.Tk()
root.geometry("700x700")
root.title('Level 3')
root.configure( bg="#67D771")


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
    q1.forget()
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



def get_artist(genre):
    if genre == pop :
        x = random.choice(pop)
    elif genre == indierock:
        x = random.choice(indierock)
    elif genre == electronic :
        x = random.choice(electronic)
    elif genre == rap :
        x = random.choice(rap)
    elif genre == latin : 
        x = random.choice(latin)
    elif genre == rnb :
        x = random.choice(rnb)
    elif genre == country :
        x = random.choice(country)
    return x 


def flick1():

    artist = get_artist(country)

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
    name = data['name']
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
        random_answer = random.sample(al_list,3)
        for i in range(3) :
            answer_list.append(random_answer[i])
        one = answer_list[0]
        two = answer_list[1]
        three = answer_list[2]
        print(answer_list)
        return one , two , three 


    #ran = random.randint(0,max-1)
    #image_url = alb_data['items'][ran]['images'][0]['url']
    #image_name = alb_data['items'][ran]['name']
    #answer_list.append(image_name)
    answers()
    i = 0 
    while True :
        if alb_data['items'][i]['name'] not in answer_list and alb_data['items'][i]['album_type'] == 'album' : 
            image_url = alb_data['items'][i]['images'][0]['url']
            image_name = alb_data['items'][i]['name']
            answer_list.append(image_name)
            break 
        else : 
            i +=1

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

    canvas = tk.Canvas(q1, width=300, height=300, bg="black", relief="solid")
    canvas.pack()

    #print(data)

    display_image(image())



    random_answer2 = random.sample(answer_list,4)


    #for o in range(4):
    #    answer_list2.append(random_answer2[o])

        
    # canvas work 
    question = 'What album is this ?'
    quesiton_label = tk.Label(q1,text= question, bg="#67D771",font=('ariel',15),foreground='black').pack()


    def chosen_option():
        choice = answer.get()
        select = ""

        if choice == answer_list[3] : 
            point.append("10")
            select = "Correct"
            print(point)
        else :
            select ="Wrong"
        
        result_label = tk.Label(q1, text=f"{choice} is {select}!")
        result_label.pack()
        
        answer.set("Select a album")
        
        return choice

    #set() est's the initial value
    answer = tk.StringVar()
    answer.set("Pick an Album ")

    #dropdownmenu syntax, tie it to a tkinter variable and a list
    dropdown = tk.OptionMenu(q1, answer, *random_answer2)

    choose_btn = tk.Button(q1, text="Click to submit", command=chosen_option)
    dropdown.pack()
    choose_btn.pack()

    button_change = tk.Button(q1,text="next question",command= change_tab1)
    button_change.pack()
    q1.pack()


def flick2():
    artist = get_artist(country)

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
    name = data['name']
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
        random_answer = random.sample(al_list,3)
        for i in range(3) :
            answer_list.append(random_answer[i])
        one = answer_list[0]
        two = answer_list[1]
        three = answer_list[2]
        print(answer_list)
        return one , two , three 


    #ran = random.randint(0,max-1)
    #image_url = alb_data['items'][ran]['images'][0]['url']
    #image_name = alb_data['items'][ran]['name']
    #answer_list.append(image_name)
    answers()
    i = 0 
    while True :
        if alb_data['items'][i]['name'] not in answer_list and alb_data['items'][i]['album_type'] == 'album' : 
            image_url = alb_data['items'][i]['images'][0]['url']
            image_name = alb_data['items'][i]['name']
            answer_list.append(image_name)
            break 
        else : 
            i +=1

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



    random_answer2 = random.sample(answer_list,4)


    #for o in range(4):
    #    answer_list2.append(random_answer2[o])

        
    # canvas work 
    question = 'What album is this ?'
    quesiton_label = tk.Label(q2,text= question, bg="#67D771",font=('ariel',15),foreground='black').pack()


    def chosen_option():
        choice = answer.get()
        select = ""

        if choice == answer_list[3] : 
            select = "Correct"
            if "10" in point : 
                point.append("20")
            else : 
                point.append("10")
        else :
            select ="Wrong"
        
        result_label = tk.Label(q2, text=f"{choice} is {select}!")
        result_label.pack()
        
        answer.set("Select a album")
        
        return choice

    #set() est's the initial value
    answer = tk.StringVar()
    answer.set("Pick an Album ")

    #dropdownmenu syntax, tie it to a tkinter variable and a list
    dropdown = tk.OptionMenu(q2, answer, *random_answer2)
    choose_btn = tk.Button(q2, text="Click to submit", command=chosen_option)

    dropdown.pack()
    choose_btn.pack()

    button_change = tk.Button(q2,text="next question",command=change_tab2)
    button_change.pack()
    q2.pack()


def flick3():
    artist = get_artist(country)

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
    name = data['name']
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
        random_answer = random.sample(al_list,3)
        for i in range(3) :
            answer_list.append(random_answer[i])
        one = answer_list[0]
        two = answer_list[1]
        three = answer_list[2]
        print(answer_list)
        return one , two , three 


    #ran = random.randint(0,max-1)
    #image_url = alb_data['items'][ran]['images'][0]['url']
    #image_name = alb_data['items'][ran]['name']
    #answer_list.append(image_name)
    answers()
    i = 0 
    while True :
        if alb_data['items'][i]['name'] not in answer_list and alb_data['items'][i]['album_type'] == 'album' : 
            image_url = alb_data['items'][i]['images'][0]['url']
            image_name = alb_data['items'][i]['name']
            answer_list.append(image_name)
            break 
        else : 
            i +=1

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



    random_answer2 = random.sample(answer_list,4)


    #for o in range(4):
    #    answer_list2.append(random_answer2[o])

        
    # canvas work 
    question = 'What album is this ?'
    quesiton_label = tk.Label(q3,text= question, bg="#67D771",font=('ariel',15),foreground='black').pack()


    def chosen_option():
        choice = answer.get()
        select = ""

        if choice == answer_list[3] : 
            select = "Correct"
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
        
        answer.set("Select a album")
        
        return choice

    #set() est's the initial value
    answer = tk.StringVar()
    answer.set("Pick an Album ")

    #dropdownmenu syntax, tie it to a tkinter variable and a list
    dropdown = tk.OptionMenu(q3, answer, *random_answer2)
    choose_btn = tk.Button(q3, text="Click to submit", command=chosen_option)

    dropdown.pack()
    choose_btn.pack()

    button_change = tk.Button(q3,text="next question",command=change_tab3)
    button_change.pack()
    q3.pack()


def flick4():
    artist = get_artist(country)

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
    name = data['name']
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
        random_answer = random.sample(al_list,3)
        for i in range(3) :
            answer_list.append(random_answer[i])
        one = answer_list[0]
        two = answer_list[1]
        three = answer_list[2]
        print(answer_list)
        return one , two , three 


    #ran = random.randint(0,max-1)
    #image_url = alb_data['items'][ran]['images'][0]['url']
    #image_name = alb_data['items'][ran]['name']
    #answer_list.append(image_name)
    answers()
    i = 0 
    while True :
        if alb_data['items'][i]['name'] not in answer_list and alb_data['items'][i]['album_type'] == 'album' : 
            image_url = alb_data['items'][i]['images'][0]['url']
            image_name = alb_data['items'][i]['name']
            answer_list.append(image_name)
            break 
        else : 
            i +=1

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



    random_answer2 = random.sample(answer_list,4)


    #for o in range(4):
    #    answer_list2.append(random_answer2[o])

        
    # canvas work 
    question = 'What album is this ?'
    quesiton_label = tk.Label(q4,text= question, bg="#67D771",font=('ariel',15),foreground='black').pack()


    def chosen_option():
        choice = answer.get()
        select = ""

        if choice == answer_list[3] : 
            select = "Correct"
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
        
        answer.set("Select a album")
        
        return choice

    #set() est's the initial value
    answer = tk.StringVar()
    answer.set("Pick an Album ")

    #dropdownmenu syntax, tie it to a tkinter variable and a list
    dropdown = tk.OptionMenu(q4, answer, *random_answer2)
    choose_btn = tk.Button(q4, text="Click to submit", command=chosen_option)

    dropdown.pack()
    choose_btn.pack()

    button_change = tk.Button(q4,text="next question",command=change_tab4)
    button_change.pack()
    q4.pack()

def flick5():
    artist = get_artist(country)

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
    name = data['name']
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
        random_answer = random.sample(al_list,3)
        for i in range(3) :
            answer_list.append(random_answer[i])
        one = answer_list[0]
        two = answer_list[1]
        three = answer_list[2]
        print(answer_list)
        return one , two , three 


    #ran = random.randint(0,max-1)
    #image_url = alb_data['items'][ran]['images'][0]['url']
    #image_name = alb_data['items'][ran]['name']
    #answer_list.append(image_name)
    answers()
    i = 0 
    while True :
        if alb_data['items'][i]['name'] not in answer_list and alb_data['items'][i]['album_type'] == 'album' : 
            image_url = alb_data['items'][i]['images'][0]['url']
            image_name = alb_data['items'][i]['name']
            answer_list.append(image_name)
            break 
        else : 
            i +=1

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



    random_answer2 = random.sample(answer_list,4)


    #for o in range(4):
    #    answer_list2.append(random_answer2[o])

        
    # canvas work 
    question = 'What album is this ?'
    quesiton_label = tk.Label(q5,text= question, bg="#67D771",font=('ariel',15),foreground='black').pack()


    def chosen_option():
        choice = answer.get()
        select = ""

        if choice == answer_list[3] : 
            select = "Correct"
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
        
        answer.set("Select a album")
        
        return choice , point 

    #set() est's the initial value
    answer = tk.StringVar()
    answer.set("Pick an Album ")

    #dropdownmenu syntax, tie it to a tkinter variable and a list
    dropdown = tk.OptionMenu(q5, answer, *random_answer2)
    choose_btn = tk.Button(q5, text="Click to submit", command= chosen_option )
    dropdown.pack()
    choose_btn.pack()

    button_change = tk.Button(q5,text="reveal your score", command= last )
    button_change.pack()
    q5.pack()


flick1()


def close():
    root.destroy()
    

final = tk.Label(last_page,text = f"You scored {point} out of 50 on the album guessing game",bg="#67D771").pack()
excit = tk.Button(last_page,text="click to close", command= close,font=('ariel',10), bg="#67D771").pack()


root.mainloop()