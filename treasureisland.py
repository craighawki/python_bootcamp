#!/usr/bin/env python

ti = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

print(ti + "\n")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

lor = input("Which way would you like to go? Left or Right? ").lower()
if lor == "right":
  print("You fall into a deep hole full of very sharp spikes and die.")
  print("Game Over! :-/")
elif lor == "left":
  print("You come up to a river.")
  river = input("Would you like to do now? Swim or Wait? ").lower()
  if river == "swim":
    print("A giant trout attacks you and eats you alive")
    print("Game over!")
  elif river == "wait":
    print("A giant turtle swims over and says jump on and takes you to the other side of the river.")
    print("When you get to the other side of the river three glowing doors appear and each one becons you, and it is very clear that you must choose one.")
    door = input("Which door do you choose? Red, Blue or Yellow? ").lower()
    if door == "blue":
      print("This was an unfortunate choice, you are eaten by a beast with huge jaws!")
      print("Game Over.")
    elif door == "red":
      print("A bright red flame burns your body to a crisp!")
      print("Game Over.")
    elif door == "yellow":
      print("You find a huge treasure!")
      print("Congratulations! You win!!!")
    else:
      print("Game Over")