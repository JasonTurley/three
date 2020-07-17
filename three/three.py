"""A library dedicated to the beauty of the number three.

"""

# Numbers

def three():
    return 3


def squared():
    return 9


def cubed():
    return 27


def dozen():
    return 36


def binary():
    return bin(3)


def factorial():
    return 6


def is_three(x):
    return x == three()


def filter(items):
    return [item for item in items if is_three(item) == True]


def map(items):
    return [three() for item in items]


def reduce(items):
    return three()    


# Currency

def dollars():
    return '$3.00'


def cents():
    return '$0.03'


# Rule of Threes
def rule_of():
    return 'Things that come in 3s are inherently more appealing.'


# Novelty 
def musketeers():
    return ['Athos', 'Aramis', 'Porthos']


def stooges():
    return ['Larry', 'Curly', 'Moe']


def wise_men():
    return ['Melchior', 'Caspar', 'Balthazar']


def little_pigs():
    """Returns a list of the materials used in the story 'Three Little Pigs'""" 
    return ['Straw', 'Sticks', 'Bricks']


# Food

def leches():
    return ['Condensed', 'Evaporated', 'Heavy cream']


def peas():
    return 'As close as three peas in a pod'