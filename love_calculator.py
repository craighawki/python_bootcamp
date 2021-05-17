#! /usr/bin/env python

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

t1_count = name1.lower().count("t")
t2_count = name2.lower().count("t")
T = t1_count + t2_count
if T == 1:
  print(f"T occurs {T} time")
else:
  print(f"T occurs {T} times")
r1_count = name1.lower().count("r")
r2_count = name2.lower().count("r")
R = r1_count + r2_count
if R == 1:
  print(f"R occurs {R} time")
else:
  print(f"R occurs {R} times")
u1_count = name1.lower().count("u")
u2_count = name2.lower().count("u")
U = u1_count + u2_count
if U == 1:
  print(f"U occurs {U} time")
else:
  print(f"U occurs {U} times")
e1_count = name1.lower().count("e")
e2_count = name2.lower().count("e")
E = e1_count + e2_count
if E == 1:
  print(f"E occurs {E} time")
else:
  print(f"E occurs {E} times")
total_1 = T + R + U + E
print(f"Total = {total_1}")

l1_count = name1.lower().count("l")
l2_count = name2.lower().count("l")
L = l1_count + l2_count
if L == 1:
  print(f"L occurs {L} time")
else:
  print(f"L occurs {L} times")
o1_count = name1.lower().count("o")
o2_count = name2.lower().count("o")
O = o1_count + o2_count
if O == 1:
  print(f"O occurs {O} time")
else:
  print(f"O occurs {O} times")
v1_count = name1.lower().count("v")
v2_count = name2.lower().count("v")
V = v1_count + v2_count
if V == 1:
  print(f"V occurs {V} time")
else:
  print(f"V occurs {V} times")
e1_count = name1.lower().count("e")
e2_count = name2.lower().count("e")
E = v1_count + v2_count
if E == 1:
  print(f"E occurs {E} time")
else:
  print(f"E occurs {E} times")
total_2 = L + O + V + E
print(f"Total = {total_2}")

print(f"your love score is {total_1}{total_2}")

love_score = (f"{total_1}{total_2}")
ls = int(love_score)
print(ls)
if ls >= 40 and ls <= 50:
  print(f"Your score is **{ls}**, you are alright together.")
elif ls < 10 or ls > 90:
  print(f"Your score is **{ls}**, you go together like coke and mentos.")
else:
  print(f"Your score is **{ls}**")