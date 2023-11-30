import random

#make a list with 3 items: rock, paper, scissors
#assign this list to a variable named 'gestures'
gestures = ['rock', 'paper', 'scissors']

repeat = True

while repeat:
    #Ask for user input and assign it to a variable named 'user' and convert it to lowercase
    user = input('Choose rock, paper, or scissors: ').lower()

    #Pick a random gesture from the list
    #Assign this gesture to a variable named 'computer'
    computer = random.choice(gestures)

    #user input validation
    if user not in gestures:
        print('Invalid input')
    else:
        
        #print user and computer gestures
        print('You chose:', user)
        print('Computer chose:', computer)

        #compare user and computer gestures
        if user == 'rock':
            if computer == 'rock':
                print('Tie')
            elif computer == 'paper':
                print('You lose')
            elif computer == 'scissors':
                print('You win')
        elif user == 'paper':
            if computer == 'rock':
                print('You win')
            elif computer == 'paper':
                print('Tie')
            elif computer == 'scissors':
                print('You lose')
        elif user == 'scissors':
            if computer == 'rock':
                print('You lose')
            elif computer == 'paper':
                print('You win')
            elif computer == 'scissors':
                print('Tie')
    
    #Ask if the user wants to play again. If yes, restart the game. If no, exit the game
    chose = input('Do you want to play again? (y/n): ').lower()
    if chose == 'y':
        repeat = True
    elif chose == 'n':
        repeat = False
    else:
        while chose != 'y' and chose != 'n':
            chose = input('Invalid input. Do you want to play again? (y/n): ').lower()


