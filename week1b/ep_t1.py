import random


def volume_cube(side):
    return side ** 3

s = 2
print "Volume of cube with side ", s, " is ", volume_cube(s)
print ""

def random_dice():
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    return dice1 + dice2

print "Sum of two random dice, rolled once: ", random_dice()
print "Sum of two random dice, rolled again: ", random_dice()
print "Sum of two random dice, rolled again: ", random_dice()
