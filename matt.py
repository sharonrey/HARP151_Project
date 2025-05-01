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


    #Now we can try requesting information
#id = "1Xyo4u8uXC1ZmMpatF05PJ" #weeknd
#id = '06HL4z0CvFAxyc27GXpf02' # taylor swift 
#id = "3TVXtAsR1Inumwj472S9r4" drake
#id = "40ZNYROS4zLfyyBSs2PGe2"  zach bryan
#id = "6KImCVD70vtIoJWnq6nGn3" #harry styles

hiphop = [
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
    "Ava Max", "Zara Larsson", "Troye Sivan", "Conan Gray", "Charlie Puth"]
rock = [
    "Coldplay", "Imagine Dragons", "Arctic Monkeys", "Queen", "Lana Del Rey",
    "The Killers", "Red Hot Chili Peppers", "Foo Fighters", "Paramore", "Green Day"] 





headers = {
    "Authorization": "Bearer " + token
}


def get_artist(genre):
    if genre == pop :
        x = random.choice(pop)
    elif genre == rock:
        x = random.choice(rock)
    elif genre == electronic :
        x = random.choice(electronic)
    elif genre == hiphop :
        x = random.choice(hiphop)
    elif genre == latin : 
        x = random.choice(latin)
    elif genre == rnb :
        x = random.choice(rnb)
    return x 

    
artist = get_artist(pop)

url = f"https://api.spotify.com/v1/artists/{id}"

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
def restart():
    
    raan = random.randint(0,max-1)
    image_name2 = alb_data['items'][raan]['name']
    answer_list.append(image_name2)


def h():
    for i in range (3):
        raan = random.randint(0,max-1)
        image_name2 = alb_data['items'][raan]['name']
        if image_name2 not in answer_list :
            image_name2 = alb_data['items'][raan]['name']
            answer_list.append(image_name2)
        else :
            restart()
    return answer_list



#h does not work 


#def otherim_name():
 #   w = 0
  #  while w < 4 :
   #     raan = random.randint(0,max-1)
    #    image_name1 = alb_data['items'][raan]['name']
     #   answer_list.append(image_name1)
      #  for i in answer_list :
       #     if i != image_name1 :
        #        answer_list.append(image_name1)
         #       w+=1
          #  else:
           #     raan = random.randint(0,max-1)
   # print(answer_list)

def image():
    ran = random.randint(0,max-1)
    image_url = alb_data['items'][ran]['images'][0]['url']
    image_name = alb_data['items'][ran]['name']
    answer_list.append(image_name)
    print(answer_list)
    print(h())
    print(data['name'])
    print(image_name)
    return image_url
    #print(image_name)
    #urllib.request.urlretrieve(image_url, f'{image_name}.jpg')
    #img = Image.open(f'{image_name}.jpg')
    #img.show()
#shows the image and prints the name of album

root = tk.Tk()
root.geometry("800x800")
root.title('Level 2')
root.configure( bg="#67D771")






#def image_name():
    #ran = random.randint(0,max-1)
    #image_url = alb_data['items'][ran]['images'][0]['url']
    #image_name = alb_data['items'][ran]['name']
    #answer_list.append(image_name)
    #return image_name 


#shows the image and prints the name of album
#top=Frame(root,background='black')
#top.grid(rowspan=2,columnspan=2)



        

    

#botton=Frame(root,background='red')
#botton.grid(rowspan=3,columnspan=3)

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

canvas = tk.Canvas(root, width=300, height=300, bg="black", relief="solid")
canvas.pack()

#print(data)

display_image(image())
root.mainloop()
