"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 10: Lists in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
import bisect

def make_word_list():
    """
        Reads lines from a file and builds a list using append.
    
        return: list of strings
    """
    # initialize variables
    a_list = []

    # open file
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        a_list.append(word)

    # Close the file
    fin.close()
    return a_list


def in_bisect(word_list, word):
    """
        Checks whether a word is in a list using bisection search.
        Precondition: the words in the list are sorted
    
        word_list: list of strings
        word: string
        
        return: boolean; True if the word is in the list, False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)


def interlock(a_list, word):
    """
        Determines if a word contains two interleavened words

        a_list: list of strings
        word: string

        return: boolean; True if a word contains two interleavened words, false otherwise
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(a_list, evens) and in_bisect(a_list, odds)


def interlock_general(a_list, word, n = 3):
    """
        Determines if a word contains 'n' interleavened words

        a_list: list of strings
        word: string
        n: integer, 3

        return: boolean; True if it contains 'n' interleavened words, false otherwise
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(a_list, inter):
            return False
    return True


print("Welcome! We're going to find all interlocked words!")

# initialize variable
word_list = make_word_list()

for word in word_list:
    if interlock(word_list, word):
        print(word, word[::2], word[1::2])

for word in word_list:
    if interlock_general(word_list, word, 3):
        print(word, word[0::3], word[1::3], word[2::3])