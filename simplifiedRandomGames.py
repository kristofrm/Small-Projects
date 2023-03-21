#Kristof Rohaly-Medved
#CS21
#Program that prompts user to roll dice or play bingo

import random

#Define main function that calls all other functions
def main():
    menu_of_options()
    option = int(input('What option do you choose? '))
    if option == 1:
        dice_roll()
    if option == 2:
         bingo()
    if option == 3:
        quit_game()
    else:
        invalid_choice(option)

#Define menu function that displays menu options
def menu_of_options():
    print('Use the numbers to select an option:')
    print('1: Roll some dice!')
    print('2: Play some Bingo!')
    print('3: Quit')

#Define dice roll function
#Get number of dice and number of sides on each die
def dice_roll():
     dice = int(input('How many dice do you want to roll? '))
     while dice <= 0:
         print('Number of dice must be greater than 0!')
         print()
         dice = int(input('How many dice do you want to roll? '))
     sides = int(input('How many sides are on each side? '))
     while sides <= 0:
         print('Number of sides must be greater than 0!')
         print()
         sides = int(input('How many sides are on each die? '))
     total = 0
     for n in range(1,dice+1):
         random_roll = random.randint(1,sides)
         print(f'Roll number {n} is {random_roll}')
         total = total + random_roll
     print(f'Total of all rolls is: {total}')
     print()
     main()

def bingo():
    #(1,75) correct?
    letter_num = random.randint(1,75)
    print()
    #Make letter = BINGO
    if letter_num < 15:
        print(f'The next number in Bingo is: B{letter_num}')
    if letter_num > 15 and letter_num <= 30:
        print(f'The next number in Bingo is: I{letter_num}')
    if letter_num > 30 and letter_num <= 45:
        print(f'The next number in Bingo is: N{letter_num}')
    if letter_num > 45 and letter_num <= 60:
        print(f'The next number in Bingo is: G{letter_num}')
    if letter_num > 60 and letter_num <= 75:
        print(f'The next number in Bingo is: O{letter_num}')
    print()
    main()

def quit_game():
    print(end = '')

def invalid_choice(choice):
    if choice > 3 or choice < 1:
        print()
        print('Please pick an option from the menu!')
        print()
        main()
    

main()
    
        
            
