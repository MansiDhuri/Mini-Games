'''
- Each time the program is run it outputs one of each of the following(at random):
    - One color(red,green,yellow,blue)
    - Left or right hand or left or right feet

'''

import random
colors = ["red","green","blue","yellow"]
body_parts = ["Left Foot","Right Foot","Left Hand","Right Hand"]

color_choice = random.choice(colors)
body_choice = random.choice(body_parts)

print("Twister Spinner says: {}, {}".format(body_choice, color_choice))
