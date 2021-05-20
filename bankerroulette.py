#!/usr/bin/env python

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

pays = random.randint(0, (len(names) - 1))
length = len(names)
print(f"Here is the length of the list: {length}")

print(f"Congratulations {names[pays]} your get to pay the bill this time.")