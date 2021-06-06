'''
Author      :
Date        :
Description :
'''
print('\033[1;32;95m |     |     /\     |\    |  ____  |\    /|     /\     |\    | ' )
print('\033[1;32;40m |     |    /  \    | \   | /    \ | \  / |    /  \    | \   | ' )
print('\033[1;32;94m |_____|   /____\   |  \  | |   _  |  \/  |   /____\   |  \  | ' )
print('\033[1;32;40m |     |  /      \  |   \ | |    \ |      |  /      \  |   \ | ' )
print('\033[1;32;93m |     | /        \ |    \| \____/ |      | /        \ |    \| ' )
#to select a random element/word from a list
from random import choice
#words to guess
fruits_file = open('fruits_list.txt', 'r') 
words = []
for line in fruits_file.readlines():
    words.append(line.replace('\n', ''))
fruits_file.close()
#select a random word from available words
word = choice(words)



print('Guess the word')


guesses = ''

#no of turns can be used
turns = 6

while turns > 0:
    #user failed times
    failed = 0

    #all charecters
    #one word at a time
    for letter in word:

        #compare that letter with guessed letter
        if letter in guesses:
            print(letter)

        else:
            print('*')
            failed += 1

    if failed == 0:
        #user will win the game
        print('\033[1;32;92m You Win')
        print('\033[1;32;40m The word is: ', word)
        break
    #if user has put a wrong letter then ask o correct it
    guess = input('guess a letter:')
    #every turn will store in guesses
    guesses += guess

    if guess not in word:
        turns -= 1
        #if the letter is guessed is wrong print wrong
        print('\033[1;31;40m Wrong')
        print('\033[1;32;92m You have', + turns, "more guesses")

        if turns == 0:
            print()
            print('\033[1;31;40m You lost! Try again..')
            print('\033[1;31;40m The word was', word)
    




    








