import random
import sys
import os
import time

# variables for coordinates
x1 = 0
y1 = 0
x2 = 0
y2 = 0
size = 0
points = 0
score_history = [1]
validate = False
valid_coords = False

# Functions for handling the file

def load_score():
    # loads the score history into a list
    file = open('scores.txt', 'r')
    lines = file.readlines()
    data = []
    for line in lines:
        aux = line.split('--@--')
        if aux[-1][-1] == '\n':
            aux[-1] = aux[-1][:-1]
        data.append(aux)
    file.close()
    return data

def save_data():
    # saves the new score data
    file = open('scores.txt', 'w')
    for line in score_history:
        record = '--@--'.join(line) + '\n'
        file.write(record)
    file.close()

def print_data():
    # prints the loaded score data
    print('\tScore', '\tDifficulty')
    for game in score_history:
        print('\t', game[0], '-' * 14 + '>' + game[1])

def print_board(size):
    # prints the card board
    print('\n ', end='')
    for i in range(size):
        print(' ', i + 1, end=' ' * 2)
    print('\n')
    for i in range(size):
        print(i + 1, end=' ')
        for j in range(size):
            if cards[i][j][1] == False:
                print('[*]  ', end='')
            else:
                if len(str(cards[i][j][0])) == 2:
                    print('[' + str(cards[i][j][0]) + '] ', end='')
                else:
                    print('[' + str(cards[i][j][0]) + ']  ', end='')
        print('\n')

def validate_size(size):
    # validates that the size is an even number
    if size > 10 or size <= 0:
        return False
    elif size % 2 == 0:
        return True
    else:
        return False

def validate_coords(row, col):
    # validates that the coordinates are within range
    # and that a letter was not entered
    limit = size - 1
    if row > limit or row < 0 or col > limit or col < 0:
        return False
    else:
        return True

def generate_numbers(size):
    # generates the list of numbers for the memory game
    list_size = size * (size // 2)
    elements1 = random.sample(range(1, list_size + 1), list_size)
    n = size
    output1 = [elements1[i:i + n] for i in range(0, len(elements1), n)]
    elements2 = elements1.copy()
    random.shuffle(elements2)
    output2 = [elements2[i:i + n] for i in range(0, len(elements2), n)]
    random.shuffle(output2)
    cards = output1 + output2
    for i in range(len(cards)):
        for j in range(len(cards[i])):
            cards[i][j] = [cards[i][j], False]
    return cards

def request_coords1():
    # asks for coordinates to flip the first card
    global valid_coords
    global x1
    global y1
    while valid_coords == False:
        print('ENTER COORDINATES ACCORDING TO THE BOARD:\n')
        try:
            x1 = int(input('Row: ')) - 1
            y1 = int(input('Column: ')) - 1
        except ValueError:
            print('Invalid input, you must enter a number')
            continue
        valid_coords = validate_coords(x1, y1)
        if valid_coords == False:
            print('Coordinates are out of range, please enter them again\n')
        elif cards[x1][y1][1] == True:
            print('Oops! That card was already flipped\n Try again...')
            x1 = 0
            y1 = 0
            request_coords1()
        else:
            cards[x1][y1][1] = True
            print_board(size)
    valid_coords = False

def request_coords2():
    # asks for coordinates to flip the second card
    global valid_coords
    global x2
    global y2
    while valid_coords == False:
        print('ENTER THE COORDINATES TO FIND THE PAIR:\n')
        try:
            x2 = int(input('Row: ')) - 1
            y2 = int(input('Column: ')) - 1
        except ValueError:
            print('Invalid input, you must enter a number')
            continue
        valid_coords = validate_coords(x2, y2)
        if valid_coords == False:
            print('Coordinates are out of range, please enter them again\n')
        elif cards[x2][y2][1] == True:
            print('Oops! That card was already flipped\n Try again...')
            x2 = 0
            y2 = 0
        else:
            cards[x2][y2][1] = True
            print_board(size)
    valid_coords = False

# initial message
print('WELCOME TO THE MEMORY GAME\
\n\nYou must enter a coordinate to flip a card\
and then another coordinate to find its pair\n')
print('To start...\n')

while validate == False:
    while True:
        try:
            size = int(input('Give me the size of the memory game (an even number): '))
            break
        except ValueError:
            print('\nInvalid input, you must enter a number\n')
            continue
    validate = validate_size(size)
    if validate == False:
        print('It must be an even number and between 2 and 10\n')

cards = generate_numbers(size)
print_board(size)

# start the game
while True:
    request_coords1()
    request_coords2()
    if cards[x1][y1][0] == cards[x2][y2][0]:
        print('WELL DONE, YOU FOUND A MATCH!!!...')
        points += 1
    else:
        cards[x2][y2][1] = False
        cards[x1][y1][1] = False
        print('Not a match....Let’s try again\n')
        points -= 1
        time.sleep(3)
        os.system('cls')
        print_board(size)

    count = 0
    for i in range(len(cards)):
        for j in range(len(cards[i])):
            if cards[i][j][1] == False:
                count += 1
    if count > 0:
        continue
    else:
        print('CONGRATULATIONS, YOU COMPLETED THE MEMORY GAME!!')
        break

print('\tSCORE HISTORY:\n')
score_history = load_score()
score_history.append([str(points), str(size) + 'x' + str(size)])
save_data()
score_history = load_score()
print_data()
time.sleep(8)
sys.exit()
