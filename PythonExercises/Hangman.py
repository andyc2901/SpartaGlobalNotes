from random_word import RandomWords
# pip3 install random-word pyyaml
# Run this is in command prompt to be able to use the random word function


def hangman(word: str):
    '''
    This function takes a random
    :param word: The word that you are trying to guess
    '''
    # word = 'hangman'
    guess = ''
    print('Be careful! If you guess more than 1 letter at once, or a number, it will take a life.')
    while len(word) != len(guess):
        guess = guess + '_'
    print(guess)

    game = True
    lives = 7
    guesses = ''
    while game:
        letter = input('Please guess a letter ')
        word_list = list(word)

        if letter in guesses:
            print('You have already guessed that letter, try again')
            print('You have ', lives, 'lives remaining')
            print('Your previous guesses are', guesses)
            print(guess)
        else:
            guesses = guesses + letter
            for ind in range(len(word_list)):
                if letter == word_list[ind]:
                    guess = list(guess)
                    guess[ind] = letter
                    guess = ''.join(guess)
            if letter in word:
                print('Well done, that was a correct letter')
                print('You have ', lives, 'remaining')
                print('Your previous guesses are', guesses)
                print(guess)
            if letter not in word:
                lives += -1
                print('Incorrect letter, you have lost a life')
                print('You have ', lives, ' lives remaining')
                print('Your previous guesses are', guesses)
                print(guess)

            if word == guess:
                print('Congratulations, you win! The word was', word)
                game = False
            if lives == 0:
                print('I win! You are out of lives. The word was', word)
                game = False


random_words = RandomWords()
hangman(random_words.get_random_word())
