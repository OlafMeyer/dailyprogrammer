#!/usr/bin/env python

def remove_letter(s, c):

    pos = s.find(c)
    return s[:pos] + s[pos + 1:]


def scrabble(rack, word):

    for letter in word:
        if letter not in rack:
            return False
        else:
            rack = remove_letter(rack, letter)
            print "active letter: " + letter
            print "rack is: " + rack

    return True
