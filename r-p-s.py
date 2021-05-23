#!/usr/bin/env python

import random
from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choice = input("What is your choice Rock, Paper or Scissors? ").lower()
comp_choice = randint(1, 3)

if your_choice == "rock":
  print(rock)
  print("You chose rock.")
  if comp_choice == 1:
    print(rock)
    print("The computer chose rock.")
    print("Draw!")
  elif comp_choice == 2:
    print(paper)
    print("The computer chose paper.")
    print("You lose!")
  else:
    print(scissors)
    print("The computer chose scissors.")
    print("You Win!")
elif your_choice == "paper":
  print(paper)
  print("You chose paper.")
  if comp_choice == 1:
    print(rock)
    print("The computer chose rock.")
    print("You win!")
  elif comp_choice == 2:
    print(paper)
    print("The computer chose paper.")
    print("Draw!")
  else:
    print(scissors)
    print("The computer chose scissors.")
    print("You Lose!")
elif your_choice == "scissors":
  print(scissors)
  print("You chose scissors.")
  if comp_choice == 1:
    print(rock)
    print("The computer chose rock.")
    print("You lose!")
  elif comp_choice == 2:
    print(paper)
    print("The computer chose paper.")
    print("You win")
  else:
    print(scissors)
    print("The computer chose scissors.")
    print("Draw!")
    