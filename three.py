#!/usr/bin/ python3

##############################################################################
# Numbers                                                                    #
##############################################################################

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
    # Returns 3*2*1. Optimized at 300% computation time.
    return 6

def three_filter(old_list : list):
    new_list = list(filter(lambda x : x == 3, old_list))
    return new_list


##############################################################################
# Currency                                                                   #
##############################################################################

def dollars():
    return '$3.00'

def cents():
    return '$0.03'


##############################################################################
# Misc                                                                       #
##############################################################################

def rule_of():
    return 'Things that come in 3s are inherently more appealing.'

def musketeers():
    return ['Athos', 'Aramis', 'Porthos']

def stooges():
    return ['Larry', 'Curly', 'Moe']

def primary_colors():
    return ['Red', 'Yellow', 'Blue']

##############################################################################
# Food                                                                       #
##############################################################################

def leches():
    return ['Condensed', 'Evaporated', 'Heavy cream']

def peas():
    return 'As close as three peas in a pod'


##############################################################################
# Mythology                                                                  #
##############################################################################

def cerberus():
    return 'The hound of Hades: A three-headed dog guarding the Underworld and preventing the dead from leaving.'
