import os
import random
import socket

import requests

URL = "https://random-word-api.herokuapp.com/word?key=K0Q4JPVF&number=1"


def is_connected():
    hostname = "www.google.com"
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(hostname)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except IOError:
        pass
    return False


def get_word():
    words = ["drop", "drug", "drum", "drunk", "dry", "due", "during", "dust", "duty", "DVD", "each", "ear", "early",
             "earn", "earth", "earthquake", "easily", "east", "eastern", "easy", "eat", "economic", "economy", "edge",
             "edit", "edition", "editor", "educate", "educated", "education", "educational", "effect", "effective",
             "effectively", "efficient", "effort", "egg", "eight", "eighteen", "eighty", "either", "elderly", "elect",
             "election", "electric", "electrical", "electricity", "electronic", "element", "elephant", "eleven", "else",
             "elsewhere", "email", "embarrassed", "embarrassing", "emerge", "emergency", "emotion", "emotional",
             "emphasis", "emphasize", "employ", "employee", "employer", "employment", "empty", "enable", "encounter",
             "encourage", "end", "ending", "enemy", "energy", "engage", "engaged", "engine", "engineer", "engineering",
             "enhance", "enjoy", "enormous", "enough", "enquiry", "ensure", "enter", "entertain", "entertainment",
             "enthusiasm", "enthusiastic", "entire", "entirely", "entrance", "entry", "environment", "environmental",
             "episode", "equal", "equally", "equipment", "error", "escape", "especially", "essay", "essential",
             "establish", "estate", "estimate", "ethical", "euro", "evaluate", "even", "evening", "event", "eventually",
             "ever", "every", "everybody", "everyday", "everyone", "everything", "everywhere", "evidence", "evil",
             "exact", "exactly", "exam", "examination", "examine", "example", "excellent", "except", "exchange",
             "excited", "excitement", "exciting", "excuse", "executive", "exercise", "exhibition", "exist", "existence",
             "expand", "expect", "expectation", "expected", "expedition", "expense", "expensive", "experience",
             "experienced", "experiment", "expert", "explain", "explanation", "explode", "exploration", "explore",
             "explosion", "export", "expose", "express", "expression", "extend", "extent", "external", "extra",
             "extraordinary", "extreme", "extremely", "eye", "face", "facility", "fact", "factor", "factory", "fail",
             "failure", "fair", "fairly", "faith", "fall", "false", "familiar", "family", "famous", "fan", "fancy",
             "fantastic", "far", "farm", "farmer", "farming", "fascinating", "fashion", "fashionable", "fast", "fasten",
             "fat", "father", "fault", "favour", "favourite", "fear", "feather", "feature", "February", "fee", "feed",
             "feedback", "feel", "feeling", "fellow", "female", "fence", "festival", "few", "fiction", "field",
             "fifteen", "fifth", "fifty", "fight", "fighting", "figure", "file", "fill", "film",
             "final", "finally", "finance", "financial", "find", "finding", "fine", "finger", "finish", "fire", "firm",
             "first", "firstly", "fish", "fishing", "fit", "fitness", "five", "fix", "fixed", "flag", "flame", "flash",
             "flat", "flexible", "flight", "float", "flood", "floor", "flour", "flow", "flower", "flu", "fly", "flying",
             "focus", "fold", "folding", "folk", "follow", "following", "food", "foot", "football", "for", "force",
             "foreign", "forest", "forever", "forget", "forgive"]

    m_word = words[random.randint(0, len(words) - 1)].lower()

    if is_connected():
        res = requests.get(URL)

        if res.status_code != 200:
            return m_word
        else:
            return res.json()[0]
    else:
        return m_word


user_guessed_word = False
word = None
guess_count = 0

letters_tried = []
guessed_letters = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_word_hints():
    global user_guessed_word, word

    user_guessed_word = True
    for c in word:
        if c in guessed_letters:
            print(c.upper(), end=""),
        else:
            user_guessed_word = False
            print("_", end=""),

    print("")


clear_screen()

max_guesses = 10
name = input("Enter your name: ")

print("Hello, %s" % name)
play_game_input = input("Are you ready to play a game of hangman (y|n)?: ")


def play_game():
    global word, user_guessed_word, guess_count, letters_tried, guessed_letters

    clear_screen()
    user_guessed_word = False
    word = get_word()
    guess_count = 0

    letters_tried = []
    guessed_letters = []

    print("Your word is %d characters long" % len(word))
    print_word_hints()
    print("")

    while True:
        if max_guesses <= guess_count:
            break

        if user_guessed_word:
            break

        print("Number of guesses remaining: %d" % (max_guesses - guess_count))
        letter = input("What is your guess: ").lower()

        clear_screen()

        if letter == "exit()":
            exit(0)

        if letter == "hint()":
            guess_count += 1

        if letter == word:
            user_guessed_word = True
            break

        if not letter.strip() or len(letter) > 1 or not letter.isalpha():
            print("You need to enter a single letter")
            print("")
            print_word_hints()
            continue

        if letter in letters_tried:
            print("You already tried that letter!")
        else:
            letters_tried.append(letter)
            if letter in word:
                guessed_letters.append(letter)
            else:
                print("The letter %s does not exists in the word" % letter)
                guess_count += 1

        print("")
        print_word_hints()

    end_screen()


def end_screen():
    global guess_count, max_guesses, user_guessed_word
    if guess_count == max_guesses:
        print("You field to guess the word %s" % word)
    elif user_guessed_word:
        print("You have successfully guess the word: %s" % word)

    replay_game_input = input("Do you want to play again (y|n)?: ")

    if not replay_game_input:
        replay_game_input = 'y'

    if replay_game_input.lower() == "y" or replay_game_input.lower() == "yes":
        clear_screen()
        play_game()
    else:
        exit(0)


if not play_game_input:
    play_game_input = 'y'

if play_game_input.lower() == "y" or play_game_input.lower() == "yes":
    clear_screen()
    play_game()
else:
    exit(0)
