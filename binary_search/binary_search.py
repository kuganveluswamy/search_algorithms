#! /usr/bin/python3


# Creates input list of numbers for the binary search algorithm
# - list of random integers in a range
# - remove the redundant elements and sort elements using set()
from random import randint

list_size = 100
number_list = [randint(1,list_size) for i in range(list_size)]
number_list = list(set(number_list))
print("The input list of numbers: {}".format(number_list))
print("The length of list of numbers: {}".format(len(number_list)))


# Creates input list of names for the binary search algorithm
# - join random alpabets to form a word
# - list of random words and sorted 
from random import choice
from string import ascii_lowercase

list_size = 100
word_size = 5
word_list = [''.join( choice(ascii_lowercase) for i in range(word_size)) for i in range(list_size)]
word_list = list(set(word_list))
word_list.sort()
print("The input list of words: {}".format(word_list))
print("The length of list of words: {}".format(len(word_list)))


# Binary search algorithm function
# - 


