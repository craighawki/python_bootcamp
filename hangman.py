#!/usr/bin/env python

#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

rand_int = random.randint(0, 2)
chosen_word = word_list[rand_int]
print(chosen_word)

guess = input("Enter a letter: ").lower()

if guess in chosen_word:
  print("Match!")
else:
  print("No Match!")