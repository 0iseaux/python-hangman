import random
import math

# basic setup
line_num = math.floor(400*random.random())

with open("allwords.txt", "r") as word_file:
    for i, line in enumerate(word_file):
        if i == line_num:
            word = line.strip()
            # print(word)

word_len = len(word)
display = '-'*word_len
guesses = []

cheers = ['Come on!', 'Keep trying!', 'You can do it!', 'You\'re getting there!'
          'Try again!', 'Almost there!!', 'Good luck!', 'Don\'t give up!']

# set difficulty level

level_set = False

y = input(
    'Welcome to the Swedish Hangman! Choose a difficulty level: [easy/normal/hard]')

while level_set == False:
    if y.lower() == 'easy':
        chance = math.ceil(word_len*3)
        level_set = True
    elif y.lower() == 'normal':
        chance = math.ceil(word_len*2)
        level_set = True
    elif y.lower() == "hard":
        chance = math.ceil(word_len*1.3)
        level_set = True
    else:
        y = input(
            'You must choose one difficulty level to begin: [easy / normal / hard]')

# input
x = input(
    'Here we go! The word is: {}! Make your first guess! [You have {} lives] (:  '.format(display, chance))


while '-' in display and display != word:

    # check input format
    if len(x) != 1:
        if len(x) > 1:
            x = input('1 letter at a time! [{} more lives]:  '.format(chance))
        if len(x) == 0:
            x = input(
                'Make a real guess! [{} more lives]:  '.format(chance))
    # register input
    else:
        chance -= 1
        if chance >= 1:
            if x in guesses and chance >= 1:
                print('You\'ve guessed \"{}\" already!'.format(x))
            if x not in guesses:
                guesses.append(x)

    # check input against word
    x = x.lower()
    if x in word:
        display = (list(display))
        for i in range(word_len):
            if word[i] == x:
                display[i] = x
        display = ''.join(display)

    # win
    if display == word:
        print('\"{}\"! Congrats! :D'.format(word))
        break

    # more input
    if chance > 1:
        j = math.floor(random.random()*len(cheers))
        x = input('{} {}! [{} more lives]:  '.format(
            display, cheers[j], chance))

    elif chance == 1:
        j = math.floor(random.random()*len(cheers))
        x = input('{} {}! [last life!]:  '.format(
            display, cheers[j]))

    # lose
    elif chance == 0:
        print('Game Over! The word is \"{}\". Bra jobbat!'.format(word))
        break
