'''
- User has to do something against the computer (e.g, Guess a random number, select random element from a list)
- Have a condition where the user can lose lives based on their guess
- User have five live as per game
- When they runout of lives the game ends and they get 'Game Over' message.

'''

from random import randint

user_lives = 5

while 1==1:
    com_num = randint(0,1)
    user_guess = int(input("Choose a number: 0 or 1"))
    print("Computer: {}, User: {}".format(com_num,user_guess))
    if user_guess == com_num:
        print("You Win !!")
    else:
        print("You Lose! You Lose a life")
        user_lives -= 1
        print("Lives left: {}".format(user_lives))
    if user_lives == 0:
        break
