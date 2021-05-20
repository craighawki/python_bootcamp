#!/usr/bin/env python

import random

choice = input("Heads or tails? ").lower()

flip = random.randint(0, 1)
result = ''

if flip == 0:
  result = "heads"
else:
  result = "tails"
if choice == result:
  print(f"{result}! You chose {choice}. You win.")
else:
  print(f"{result}! You chose {choice}. You lose.")