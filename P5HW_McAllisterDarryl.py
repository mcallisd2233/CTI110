#CTI-110 P5HW - Math Quiz
#Darryl McAllister
#5/3/2023
#A menu program that simulates a simple math quiz

import random

rnum = random.randint(100, 200)

print("Welcome to Math Quiz")

def print_menu():
    print("\nMAIN MENU")
    print('---------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit\n')

quit_quiz = False

while not quit_quiz:
    rnum1 = random.randint(1, 201)
    rnum2 = random.randint(1, 201)
    print_menu()
    choice = int(input('Please choose one of the menu options: '))
    if choice == 1:
        guess = 0
        print(' ', rnum1)
        print('+', rnum2)
        rnum_sum = rnum1 + rnum2
        user_int1 = int(input('Enter answer.\n'))
        while user_int1 != rnum_sum:
            if user_int1 < rnum_sum:
                print('Sorry, guess is too low.')
                guess += 1
            if user_int1 > rnum_sum:
                print('Sorry, guess is too high.')
                guess += 1
            user_int1 = int(input('Try again: '))
        if user_int1 == rnum_sum:
            print('Congratulations!!! Your answer is correct.')
            guess += 1
            print('Number of guesses: ', guess)
    if choice == 2:
        guess = 0
        print(' ', rnum1)
        print('-', rnum2)
        rnum_sum = rnum1 - rnum2
        user_int2 = int(input('Enter answer.\n'))
        while user_int2 != rnum_sum:
            if user_int2 < rnum_sum:
                print('Sorry, guess is too low.')
                guess += 1
            if user_int2 > rnum_sum:
                print('Sorry, guess is too high.')
                guess += 1
            user_int2 = int(input('Try again: '))
        if user_int2 == rnum_sum:
            print('Congratulations!!! Your answer is correct.')
            guess += 1
            print('Number of guesses: ', guess)
    if choice == 3:
        print('Thank you for playing ...')
        print('Bye!')
        quit_quiz = True
    if choice < 1 or choice > 3:
        print('ERROR!!!!! Please enter a valid menu option!!')

                
        
        
        
