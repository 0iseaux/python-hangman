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
miss = 0
diagram = {
    0: '',
    1: '    |',
    2: '    |\n    |',
    3: '    |\n    |\n    |',
    4: '    |\n    |\n    |\n    |',
    5: '    |\n    |\n    |\n    |\n    |',
    6: '    _\n    |\n    |\n    |\n    |\n    |',
    7: '    __\n    |\n    |\n    |\n    |\n    |',
    8: '    ___\n    |\n    |\n    |\n    |\n    |',
    9: '    ____\n    |\n    |\n    |\n    |\n    |',
    10: '    _____\n    |\n    |\n    |\n    |\n    |',
    11: '    ______\n    |\n    |\n    |\n    |\n    |',
    12: '    ______\n    |/\n    |\n    |\n    |\n    |',
    13: '    ______\n    |/  |\n    |\n    |\n    |\n    |',
    14: '    ______\n    |/  |\n    |  (\n    |\n    |\n    |',
    15: '    ______\n    |/  |\n    |  ( )\n    |\n    |\n    |',
    16: '    ______\n    |/  |\n    |  (_)\n    |\n    |\n    |',
    17: '    ______\n    |/  |\n    |  (_)\n    |   |\n    |\n    |',
    18: '    ______\n    |/  |\n    |  (_)\n    |  \\|\n    |\n    |',
    19: '    ______\n    |/  |\n    |  (_)\n    |  \\|/\n    |\n    |',
    20: '    ______\n    |/  |\n    |  (_)\n    |  /|\\\n    |  /\n    |',
    21: '    ______\n    |/  |\n    |  (_)\n    |  /|\\\n    |  / \\\n    |',
}

cheers = ['Come on!', 'Keep trying!', 'You can do it!', 'You\'re getting there!'
          'Try again!', 'Almost there!!', 'Good luck!', 'Don\'t give up!']

# set difficulty level

level_set = False

y = input(
    'Welcome to the Swedish Hangman! Choose a difficulty level: [easy/normal/hard]')

while level_set == False:
    if y.lower() == 'easy':
        # chance = math.ceil(word_len*3)
        level_set = True
    elif y.lower() == 'normal':
        # chance = math.ceil(word_len*2)
        level_set = True
    elif y.lower() == "hard":
        # chance = math.ceil(word_len*1.3)
        level_set = True
    else:
        y = input(
            'You must choose one difficulty level to begin: [easy / normal / hard]')

# input
x = input(
    'Here we go! The word is {}! Make your first guess!\t'.format(display))


while '-' in display and display != word:

    # check input format
    while len(x) != 1:
        if len(x) > 1:
            x = input('1 letter at a time!:\t'.format)
        if len(x) == 0:
            x = input(
                'Make a real guess!:\t')

    # register input
    if miss < 21:
        if x in guesses:
            if x not in word:
                print('\nOops!You\'ve guessed \"{}\" already!'.format(x))
            else:
                print(
                    '\nHey!You\'ve guessed \"{}\" already (though it was correct)!'.format(x))
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
    else:
        miss += 1

    # win
    if display == word:
        print('\n{}\"{}\"!\nCongrats! You\'ve saved a life! :D'.format(
            diagram[miss], word))
        break

    # prompt for more input
    if miss < 21:
        j = math.floor(random.random()*len(cheers))
        x = input('{}\n{}!\nThe word is: {}\t'.format(
            diagram[miss], cheers[j], display))

    # lose
    elif miss == 21:
        print('\n{}\nGame Over! The word is \"{}\". Bra jobbat!'.format(
            diagram[miss], word))
        break
