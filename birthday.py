"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 10: Lists in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
import random

def has_duplicates(a_list):
    """
        Determine if a list has duplicates

        a_list: list

        return: boolean; True if has duplicates, false otherwise
    """
    # initialize a list and sort it. This prevents modifying the original list
    b_list = list(a_list)
    b_list.sort()

    # check for adjacent elements that are equal
    for i in range(len(b_list) - 1):
        if b_list[i] == b_list[i+1]:
            return True
    return False


def random_birthdays(n):
    """
        Generate a list of 'n' number of random birthdays

        n: int

        return: list; list of with 'n' birthdays
    """
    birthdays = []
    for i in range(n):
        bday = random.randint(1, 365)
        birthdays.append(bday)
    return birthdays


def count_matches(number_students, number_simulations):
    """
        Generate a sample of birthdays and counts the number of those that have duplicates

        number_students: int
        number_simulations: int

        return: int; the number of matches
    """
    # initialize variables
    count = 0
    for i in range(number_simulations):
        a_list = random_birthdays(number_students)
        if has_duplicates(a_list):
            count += 1
    return count

def user_input():
    """
        Ask for user input to try out the number of matching birthdays for a user-provided number of students and simulations
    """
    print("Welcome to the random matching birthday counter.")
    num_students = int(input("Please enter the number of students in the classroom: "))
    num_simulations = int(input("Please enter the number of simulations to run: "))

    count = count_matches(num_students, num_simulations)
    print("For %d simulations with %d students, there were %d simulations with at least one match." % (num_simulations, num_students, count))

user_input()