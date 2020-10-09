"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 10: Lists in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
import time

def make_word_list_append():
    """
        Reads lines from a file and builds a list using append

        return: list
    """
    # initialize variables
    a_list = []

    # open the file
    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        a_list.append(word)
    
    # clsose the file
    fin.close()
    
    return a_list

def make_word_list_add():
    """
        Reads lines from a file and builds a list using +

        return: list
    """
    # initialize variables
    a_list = []

    # open the file
    fin = open("words.txt")
    
    for line in fin:
        word = line.strip()
        a_list += [word]
    
    # clsose the file
    fin.close()

    return a_list

start_time_1 = time.time()
a_list = make_word_list_append()
elapsed_time_append = time.time() - start_time_1

start_time_2 = time.time()
b_list = make_word_list_add()
elapsed_time_add = time.time() - start_time_2

print("Let's test out two functions for appending to a list.")
print(len(a_list))
print(a_list[:10])
print("It takes %d seconds to append using the .append function." % (elapsed_time_append))
print(len(b_list))
print(b_list[:10])
print("It takes %d seconds to append using the + function." % (elapsed_time_add))