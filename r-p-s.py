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

your_choice = input("What is your choice   Rock, Paper or Scissors? ").lower()
comp_choice = randint(1, 3)

if your_choice == "rock":
  print(rock)
  if comp_choice == 1:
    print(rock)
    print("Draw!")
  elif comp_choice == 2:
    print(paper)
    print("You lose")
  else:
    print(scissors)
    print("You Win!")
elif your_choice == "paper":
  print(paper)
  if comp_choice == 1:
    print(rock)
    print("You win!")
  elif comp_choice == 2:
    print(paper)
    print("Draw!")
  else:
    print(scissors)
    print("You Lose!")
elif your_choice == "scissors":
  print(scissors)
  if comp_choice == 1:
    print(rock)
    print("You win!")
  elif comp_choice == 2:
    print(paper)
    print("You lose")
  else:
    print(scissors)
    print("Draw!")