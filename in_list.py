"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 10: Lists in Think Python 2
    
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


def in_bisect_cheat(word_list, word):
    """
        Checks whether a word is in a list using bisection search.
        Precondition: the words in the list are sorted
    
        word_list: list of strings
        word: string
        
        return: boolean; True if the word is in the list, False otherwise
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


word_list = make_word_list()
    
for word in ['aa', 'alien', 'allen', 'zymurgy']:
    print("Using the regular bisect method, the word: " + word + ' is in list: ', in_bisect(word_list, word))

for word in ['aa', 'alien', 'allen', 'zymurgy']:
    print("Using the cheat bisect method, the word: " + word + ' is in list: ', in_bisect(word_list, word))