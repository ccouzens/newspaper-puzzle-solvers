#!/usr/bin/env python

game = [
    [None, 1, 6, None, 2, None, None, None, None],
    [5, None, 4, 6, 1, 9, None, None, 3],
    [None, None, 2, 5, 7, None, 9, 6, None],
    [None, None, 7, None, 4, None, None, 9, 5],
    ([None] * 9), 
    [3, 4, None, None, 9, None, 7, None, None],
    [None, 6, 9, None, 8, 7, 5, None, None],
    [1, None, None, 9, 5, 3, 6, None, 4],
    [None, None, None, None, 6, None, 8, 1, None]
]

def print_game(game):
    for y in xrange(9):
        line = game[y]
        for x in xrange(9):
            digit = line[x]
            if digit==None:
                print ' ',
            else:
                print digit,
            if x in [2,5]:
                print '|',
        print
        if y in [2,5]:
            print '------+-------+-------'

def check_game_valid(game):
    for y in xrange(9):
        line = game[y]
        for x in xrange(9):
            digit = line[x]
            if digit != None and not (digit >= 1 and digit <= 9):
                return False
    for c in xrange(9):
        if not check_horizontal_line(game, c):
            return False
        if not check_vertical_line(game, c):
            return False
        if not check_square(game, c/3, c%3):
            return False
    return True

def check_9_numbers(numbers):
    for i in xrange(9):
        digit = numbers[i]
        if digit != None and digit in numbers[i+1:]:
            return False
    return True


def check_horizontal_line(game, y):
    numbers = game[y]
    return check_9_numbers(numbers)

def check_vertical_line(game, x):
    numbers = [line[x] for line in game]
    return check_9_numbers(numbers)

def check_square(game, x, y):
    numbers = sum( [line[x*3:x*3+3] for line in game[y*3:y*3+3]], [])
    return check_9_numbers(numbers)

print_game(game)
print check_game_valid(game)
