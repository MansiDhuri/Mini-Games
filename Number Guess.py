'''
- Create the same number guessing game as before (computer randomly generates a number, user has to guess)
- Make it so that the user only has to run the programme and can keep guessing until they get it right

'''

import random
computer_num = random.randint(1,100)
print(computer_num)

while 'play' == 'play':
    user_guess = int(input("Guess the number :"))
    if user_guess == computer_num:
        print("You Win !!!")
        break
    elif user_guess > computer_num:
        print("To High!!")
    else:
        print("To Low!!")
print("Your guess was: {}, computer guess was: {}".format(user_guess,computer_num))
