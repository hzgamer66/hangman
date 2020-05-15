import random, sys

word_list = ['integer', 'string', 'boolean', 'float', 'double', 'character', 'set',
             'dictionary', 'list', 'binary', 'value',]  # the words

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']  # the allowed characters

print("Let's play hangman!")


def play_hangman():
    word = random.choice(word_list)  # chooses random word
    lives = 6
    guessed_characters = []  # list of guessed characters
    secret_word = []  # variable used to later make the blanks (______)

    for x in range(len(word)):  # adds _ as many times as needed to the secret word
        secret_word.append(' _ ')

    while lives > 0:
        print('')  # to add a blank space to prevent clutter
        print(*secret_word, sep="")
        print('Lives left: ' + str(lives))
        print('Guess a letter (type "help" to see what you\'ve already guessed'
              ' or "guess answer" to have one shot to guess (if it\'s wrong it\'s game over!)).')
        guessed_letter = input()
        guessed_letter = guessed_letter.lower()  # makes it lowercase

        if guessed_letter == 'help':  # extra credit part 1 (determine if help was typed)
            print(*guessed_characters, sep=', ')
            continue
        elif guessed_letter == "guess answer":  # extra credit part 2 (determines if guess answer was typed)
            print('')
            print('What do you think the answer is?')
            answer_guess = input()
            answer_guess = answer_guess.lower()
            if answer_guess == word:
                print('')
                print('You guessed correctly!')
                play_again()
                break
            elif answer_guess != word:
                print('')
                print('Your guess is incorrect. Game over!')
                play_again()
                break
        elif guessed_letter not in alphabet:  # verifies that the input is a valid option
            print('Invalid character.')
            continue
        elif guessed_letter in guessed_characters:  # verifies that input has not already been guessed
            print('You have already guessed that character.')
            continue

        guessed_characters.append(guessed_letter)  # adds letter to list of already guessed letters

        if guessed_letter in word:  # if the letter is in the word
            for y in range(len(word)):
                if word[y] == guessed_letter.lower():  # determines where in the word the letter is used
                    secret_word[y] = guessed_letter.lower()  # replaces that location in secret_word with letter
        elif guessed_letter not in word:  # if the letter is NOT in the word
            print('Letter not found')
            lives = lives - 1

        if ' _ ' not in secret_word:  # determines when the puzzle is solved
            print('')
            print(*secret_word, sep="")
            print("Word guessed, you've won!")
            play_again()
            break

    if lives <= 0:  # if you run out of lives
        print('')
        print('Out of lives, game over!')
        play_again()


def play_again():  # asks if you want to play again or not
    while True:
        print('Play again? (yes/no)')
        play_again_response = input().lower()  # Yes -> yes and No -> no, etc.
        if play_again_response == 'yes':
            print('New game!')
            break
        elif play_again_response == 'no':
            sys.exit()  # leave
        else:
            print('Invalid input.')  # if any other input occurs


# start!
while True:
    play_hangman()
