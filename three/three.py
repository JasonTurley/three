"""A library dedicated to the beauty of the number three.

"""
from datetime import timedelta, date, datetime

import itertools

# Numbers

def three():
    return 3


def squared():
    return 9


def cubed():
    return 27


def dozen():
    return 36


def hundred():
    return 300


def thousand():
    return 3000


def million():
    return 3000000


def binary():
    return bin(3)


def factorial():
    return 6


def is_three(x):
    return x == three()


def filter(items):
    return [item for item in items if is_three(item)]


def map(items):
    return [three() for item in items]


def reduce(items):
    return three()

def threes():
    while True:
        yield 3

def n_threes(n):
    return list(itertools.islice(threes(), n))

def decimal_places(i):
    return '{:.3f}'.format(i)


def days_ago(timestamp):
    return timestamp - (86400 * 3)

def third_element(items):
	try:
		return items[three()-1]
	except Exception as exp:
		return exp


# Units


def g(i):
    return i + 'g'


def kg(i):
    return i + 'kg'


def mm(i):
    return i + 'mm'


def cm(i):
    return i + 'cm'


def m(i):
    return i + 'm'


def km(i):
    return i + 'km'


# Language

def letters():
    return ['t', 'h', 'r', 'e', 'e']


def spanish():
    return 'tres'


def german():
    return 'drei'


def french():
    return 'drois'


def italian():
    return 'tre'


# Currency

def dollars():
    return '$3.00'


def cents():
    return '$0.03'


def euros():
    return '€3.00'


# Rule of Threes

def rule_of():
    return 'Things that come in 3s are inherently more appealing.'


def is_appealing(items):
    return len(items) == 3


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


def blind_mice():
    """Returns the names of the three blind mice in shrek"""
    return ['Forder', 'Gorder', 'Horder']


def kingdoms():
    """Returns the tripartite division of China from 220–280 AD"""
    return ['Wei', 'Shu', 'Wu']


def some():
    return '3 people having fun ;)'


# Food

def leches():
    return ['Condensed', 'Evaporated', 'Heavy cream']


def peas():
    return 'As close as three peas in a pod'

# Misc

def string():
    return '3'

def force_three(func):
    def inner(*args, **kwargs):
        return three()
    return inner


class ThreeMeta(type):
    def __getattr__(self, _):
        return three()

'''
3
'''
class Three(metaclass=ThreeMeta):
    def __getattr__(self, _):
        return three()

    def __repr__(self):
        return string()

    def __str__(self):
        return string()

def o_clock():
    return '🕒'

# Date time

def hours_from_now():
    return (datetime.now() + timedelta(hours=3)).strftime('%H:%M:%S')

def days_from_now():
    return (date.today() + timedelta(days=3)).strftime('%d %B %Y')
