'''
- Create a program that simulate two dice being rolled
- In the program give a message to the user saying what two dice value are and their combined total 

'''

import random
num_one = random.randint(1,6)
num_two = random.randint(1,6)
print(num_one,num_two)

dice_total = num_one + num_two

print("Dice simulator complete! Num one: {}, Num two: {}. Total is: {}".format(num_one,num_two,dice_total))
