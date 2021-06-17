#!/usr/bin/env python

import math

test_h = int(input("What is the height of the wall in meters?: "))
test_w = int(input("what is the width of the wall in meters? "))


def coverage(test_h, test_w):
    cans = math.ceil((test_h * test_w) / 5)
    print(f"Since hour area height is {test_h} meters and the width is {test_w} meters,")
    print(f"You will need {cans} cans of paint.")
coverage(test_h, test_w) 
