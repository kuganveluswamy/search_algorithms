#! /usr/bin/python3

from random import randint
from random import choice
from string import ascii_lowercase

# Binary search algorithm function
# - needs a sorted list to work
# - middle element is comapred to the desired element
# - left and right pointers are moved based eleminating half of the list
# - middle pointer is calculated based on new left and right pointers
# - returns the position of the desired element or returns -1 when absent

def binary_search(mylist, data):
  left   = 0
  right  = len(mylist)-1
  while left <= right:
    middle = ((right-left) // 2) + left
    # print("left= {}  middle= {}  right= {}".format(left, middle, right))
    if mylist[middle] == data:
      return middle
    elif mylist[middle] > data:
      right = middle-1
    elif mylist[middle] < data:
      left = middle+1
  return -1

if __name__ == "__main__":
  # Creates input list of numbers for the binary search algorithm
  # - list of random integers in a range
  # - remove the redundant elements and sort elements using set()
  list_size = 100
  number_list = [randint(1,list_size) for i in range(list_size)]
  number_list = list(set(number_list))
  print("The input list of numbers: {}".format(number_list))
  print("The length of list of numbers: {}\n".format(len(number_list)))

  # Creates input list of names for the binary search algorithm
  # - join random alpabets to form a word
  # - list of random words and sorted 
  list_size = 100
  word_size = 5
  word_list = [''.join( choice(ascii_lowercase) for i in range(word_size)) for i in range(list_size)]
  word_list = list(set(word_list))
  word_list.sort()
  print("The input list of words: {}".format(word_list))
  print("The length of list of words: {}\n".format(len(word_list)))

  # Testing with number_list  
  test_num = 150
  print("Position of {} in number_list: {}".format(test_num, binary_search(number_list, test_num)))	# expected -1
  for i in range(5):
    test_num = number_list[randint(0,len(number_list))]
    print("Position of {} in number_list: {}".format(test_num, binary_search(number_list, test_num)))
  print("\n")

  # Testing with word_list  
  test_word = 'abcdef'
  print("Position of {} in word_list: {}".format(test_word, binary_search(word_list, test_word))) 	# expected -1
  for i in range(5):
    test_word = word_list[randint(0,len(word_list))]
    print("Position of {} in word_list: {}".format(test_word, binary_search(word_list, test_word)))
