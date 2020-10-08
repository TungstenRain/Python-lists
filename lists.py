"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 10: Lists in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def nested_sum(int_list):
    """
        Sum the list of lists of integers

        int_list: list of lists of integers

        return: int; summation of all the integers
    """
    total = 0
    for in_list in int_list:
        total += sum(in_list)
    return total


def cum_sum(int_list):
    """
        Take a list of integers and replace each indexed value with the cumulative sum of the values in the list

        int_list: list of integers

        return: list of integers with cumulative sum of values
    """
    # initialize variables
    total = 0
    result = []
    for x in int_list:
        total += x
        result.append(total)
    return result


def middle(a_list):
    """
        Take a list and return all but the first and last elements

        a_list: list

        return: list with all but the first and last elements
    """
    return a_list[1:-1]


def chop(a_list):
    """
        Take a list, modifies it so it removes the first and last elements and returns None

        a_list: list

        return: None
    """
    del(a_list[0])
    del(a_list[-1])


def is_sorted(a_list):
    """
        Take a list and returns True if the list is sorted

        a_list: list

        return: boolean; True if sorted, false otherwise
    """
    return a_list == sorted(a_list)


def is_anagram(word_1, word_2):
    """
        Determine if two words are anagrams of each other

        word_1: string
        word_2: string

        return: boolean; True if the words are anagrams, false otherwise
    """
    return sorted(word_1) == sorted(word_2)

print(str(is_anagram("hello", "ohell")))
print(str(is_anagram("hello", "o hell")))


def has_duplicates(a_list):
    """
        Determine if a list has duplicates

        a_list: list

        return: boolean; True if it has duplicates, false otherwise
    """
    # initialize a list and sort it. This prevents modifying the original list
    b_list = list(a_list)
    b_list.sort()

    # check for adjacent elements that are equal
    for i in range(len(b_list) - 1):
        if b_list[i] == b_list[i+1]:
            return True
    return False



list_1 = [[1,2], [3], [4,5,6]]
list_2 = [1, 5, 6]
list_3 = [1, 6, 10, 13, 1, 5, 7]
list_4 = [1, 6, 10, 13, 1, 5, 7]
list_5 = [1, 6, 10, 13, 1, 5, 7]
list_6 = [1, 6, 10, 13, 21, 25, 27]
list_7 = [1, 6, 10, 13, 1, 5, 7]
list_8 = [1, 6, 10, 13, 21, 25, 27]


print(str(nested_sum(list_1)))
print(str(cum_sum(list_2)))
print(str(middle(list_3)))
print(str(chop(list_4)))
print(list_4)
print(str(is_sorted(list_5)))
print(str(is_sorted(list_6)))
print(str(has_duplicates(list_7)))
print(str(has_duplicates(list_8)))