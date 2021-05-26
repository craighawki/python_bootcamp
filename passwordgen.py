#!/usr/bin/env python

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
count_1 = 0
count_2 = 0
count_3 = 0
passw = []

for letter in letters:
  count_1 += 1
  if count_1 <= nr_letters:
    passw.append(random.choice(letters))
    lets_a =(random.choice(letters))
lets = lets_a

for number in numbers:
  count_2 += 1
  if count_2 <= nr_numbers:
    passw.append(random.choice(numbers))
    nums_a = (random.choice(numbers))
nums = nums_a
    
for symbol in symbols:
  count_3 += 1
  if count_3 <= nr_symbols:
    passw.append(random.choice(symbols))
    syms_a = (random.choice(symbols))
syms = syms_a

passout = ""
print(passw)
for ele in passw:
  passout += ele
print(f"Here is your password: {passout}")
