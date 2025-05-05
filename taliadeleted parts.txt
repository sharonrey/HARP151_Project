decades = {
    '1980s': ('1980-01-01', '1989-12-31'),
    '1990s': ('1990-01-01', '1999-12-31'),
    '2000s': ('2000-01-01', '2009-12-31'),
    '2010s': ('2010-01-01', '2019-12-31'),
    '2020s': ('2020-01-01', '2029-12-31')
}

# Initialize Tkinter window
root = tk.Tk()
root.title("Spotify Guessing Game")
root.geometry("600x600")

# Variables
selected_genre = tk.StringVar()
selected_decade = tk.StringVar()
score = 0
question_label = None
option_buttons = []
album_label = None

# Function to get random album with exclusions
def get_random_album(genre, decade, exclude_album_names=None):
    if exclude_album_names is None:
        exclude_album_names = []

    artists = genres.get(genre, [])
    if not artists:
        return None, None

    artist = random.choice(artists)
    results = sp.search(q=f"artist:{artist}", type="album", limit=10)
    albums = results['albums']['items']

    albums_with_images = [album for album in albums if album['images'] and album['name'] not in exclude_album_names]

    if not albums_with_images:
        return None, None

    album = random.choice(albums_with_images)
    album_name = album['name']
    album_image_url = album['images'][0]['url']

    return album_name, album_image_url

# Function to check the answer
def check_answer(selected_option):
    global score
    if selected_option == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "Well done! That's the right answer.")
    else:
        messagebox.showinfo("Wrong!", f"Oops! The correct answer was {correct_answer}.")
    for btn in option_buttons:
        btn.destroy()
    if album_label:
        album_label.destroy()
    load_level_3_question()

# Load question for level 3
def load_level_3_question():
    global correct_answer, album_label, option_buttons

    correct_answer, album_image_url = get_random_album(selected_genre.get(), selected_decade.get())
    if not correct_answer or not album_image_url:
        messagebox.showerror("Error", "Could not retrieve album. Try again.")
        return

    response = requests.get(album_image_url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize((300, 300), Image.LANCZOS)
    album_img = ImageTk.PhotoImage(img)

    album_label = tk.Label(root, image=album_img)
    album_label.image = album_img
    album_label.pack(pady=10)

    options = [correct_answer]
    attempts = 0
    max_attempts = 20

    while len(options) < 4 and attempts < max_attempts:
        fake_answer, _ = get_random_album(selected_genre.get(), selected_decade.get(), exclude_album_names=options)
        if fake_answer and fake_answer not in options:
            options.append(fake_answer)
        attempts += 1

    if len(options) < 4:
        messagebox.showerror("Error", "Couldn't generate enough unique album names. Try again.")
        return

    random.shuffle(options)

    option_buttons = []
    for option in options:
        btn = tk.Button(root, text=option, command=lambda opt=option: check_answer(opt))
        btn.pack(pady=5)
        option_buttons.append(btn)

def play_game():
    genre_menu.pack_forget()
    decade_menu.pack_forget()
    play_button.pack_forget()
    load_level_3_question()