#!/usr/bin/env python

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇  
tot = 0
count = 0
for num in student_heights:
    count += 1
    tot += num
print(tot)
print(count)
avg = int(tot / count)
print(f"The average height is {avg} centimeters.")