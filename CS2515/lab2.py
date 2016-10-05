import time
import random

def reverseStack(stack):

    """A function which, when given a stack as input,
    will return a new stack with all the elements in reverse order. """

    r_stack = []
    while len(stack) > 0:
        reverse = stack.pop()
        r_stack.append(reverse)
    return r_stack

def nestedAndBalanced(string):

    """A function which takes a character string as input, and determines
    whether or not the brackets - [, ], {, }, (, ) - are properly nested and
    balanced using a stack. """

    left = '[{('
    right = ']})'

    b_stack = []

    rnd = ('(',')')
    sqr = ('[',']')
    curly = ('{','}')
    
    for item in string:
        if item in right and len(b_stack) == 0:
            return False
        if item in left:
            b_stack.append(item)
        elif item in right:
            last = b_stack.pop()
            if last in rnd and item in rnd:
                correct = True
            elif last in sqr and item in sqr:
                correct = True
            elif last in curly and item in curly:
                correct = True
            else:
                return False
    if len(b_stack) != 0:
        return False
    return correct

def colouredTetris():

    block = []
    colours = ['red', 'green', 'blue']
    for _ in range(20):
        block.append(random.choice(colours))

    tetris = []
    tetris.append(block[0])
    print("|%-9s|" % (tetris[0]))
    print("|---------|")

    i = 1
    k = 5
    contin = None
    points = 0
    while i < len(block):
        before = time.time()
        contin = input("The next block is %s. Do you want it? (y/n)" % (block[i]))
        after = time.time()
        if (after - before) > k:
            tetris.append(block[i])
            print("Sorry you took longer than %i seconds to answer. The block has been added." %(k))
        else:
            if contin != 'n' and contin != 'y':
                contin = input("Please answer y or n only. The next block is %s. Do you want it?" % (block[i]))
            else:
                if contin == 'n':
                    pass
                elif contin == 'y':
                    try:
                        if tetris[-1] == block[i]:
                            points += 1
                            tetris.pop()
                            print('You made a match!')
                        else:
                            tetris.append(block[i])
                    except IndexError:
                        tetris.append(block[i])
            for item in reversed(tetris):
                print("|%-9s|" % (item))
                print("|---------|")
        i += 1
    if len(tetris) > 0:
        points -= len(tetris)
    print("GAME OVER - You scored %i points" % (points))
