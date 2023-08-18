# WORD GUESSING GAME

import requests
from random import choice

def get_country_names():
    response = requests.get("https://restcountries.com/v3.1/all?fields=name,flags`")       # The site and code to get all country names
    countries = response.json()
    country_names = [country["name"]["common"] for country in countries]
    return country_names

'''
Since we are already calling this function in the 'while True' loop, 
we are already using the result of this function in the game. 
So we don't need to call the function 'get_country_names()' again.

'''

while True:
    print("#" * 80)
    print("#" * 30 + " WORD GUESSING GAME " + "#" * 30)
    print("#" * 80)

    country_names = get_country_names()
    word = choice(country_names).upper()              # Recognizes all letters as uppercase
    lettercount = len(word)
    print("\nThe word has {} letters.".format(lettercount))

    forecasts = []      # A list to store correctly guessed letters
    error = []          # A list to store incorrectly guessed letters
    experiment = 7

    while experiment > 0:
        signboard = ""
        for letter in word:
            if letter in forecasts:
                signboard += letter
            else:
                signboard += "_"

        if signboard == word:
            print("You got the word right. Congratulations!")
            print("The word: {}".format(word))
            break

        print("Guess the word", signboard)
        print("You've got", experiment, "lives")

        guess = input("Enter one letter: ")
        guess = guess.upper()

        if guess == word:
            print("You got it right!")
            break

        if guess in forecasts or guess in error:
            print("{} has already been said. Please say another letter.".format(guess))
        elif guess in word:
            rpt = word.count(guess)
            print("Correct! The letter {} appears {} times in the word.".format(guess, rpt))
            forecasts.append(guess)
        else:
            print("Wrong guess. The letter {} does not exist in our word.".format(guess))
            error.append(guess)
            experiment -= 1
        
    if experiment == 0:
        print("You have no rights left. You've failed.")
        print("The word: {}".format(word))

    tocontinue = input("Press 'q' to exit the game or any key to continue: ")
    tocontinue = tocontinue.lower()
    if tocontinue == "q":
        print("You're out of the game!")
        break
