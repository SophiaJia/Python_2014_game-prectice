"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    new_list = []
    if len(list1)>1 :
        new_list.append(list1[0])
        for dummy_i in range(1, len(list1)):
          if list1[dummy_i] != list1[dummy_i-1]:
            new_list.append(list1[dummy_i])        
    elif len(list1) < 2:
        new_list = list1
    return new_list 


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    dummy_i = 0 
    new_list = []
    while dummy_i < len(list1):
          if list1[dummy_i] in list2:
                new_list.append(list1[dummy_i])
          dummy_i += 1    
    new = remove_duplicates(new_list)
    return new

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    dummy_i = 0 
    dummy_j = 0
    new_list = []
    while dummy_i < len(list1) and dummy_j < len(list2):
          if list1[dummy_i] <= list2[dummy_j]:
                new_list.append(list1[dummy_i])
                dummy_i += 1
          else:
                new_list.append(list2[dummy_j])
                dummy_j += 1            
            
    if dummy_i < len(list1):
       new_list.extend(list1[dummy_i:])
    if dummy_j < len(list2):
       new_list.extend(list2[dummy_j:])
    return new_list

                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    new_list = []
    if len(list1)== 1:
       return list1
    if len(list1) == 2:
        if list1[0] > list1[1]:
            new_list.append(list1[1])
            new_list.append(list1[0])
        else :
            new_list = list1
        return new_list 
    if len(list1) > 1:
        length = len(list1)        
        new1 = merge_sort(list1[0:length/2])
        new2 = merge_sort(list1[length/2 : length])
        new_list = merge(new1, new2)
         
    return new_list

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    length = len(word)
    new_list = []
    if length == 0:
        new_list.append('')
        return new_list
        
    if length == 1:
        new_list.append('')
        new_list.append(word)
        return new_list
       
    first = word[0]
    rest  = word[1 : length]
    rest_strings = gen_all_strings(rest)
    new_list.extend(rest_strings)
    for dummy_str in rest_strings:
        #print new_list
        #if dummy_str != "" :
           #new_word = first + dummy_str
           #new_list.append(new_word)
        #  new_list.append(dummy_str)
        dummy_i = 0
        while dummy_i <= len(dummy_str):
            #print "new_first", dummy_str[0:dummy_i]
            #print "dummy_i", dummy_i
            new_first = str(dummy_str[0:dummy_i]) + first
            #print  "new_first", new_first
            new_word  = new_first + str(dummy_str[dummy_i:])
            #print "the new word", new_word
            dummy_i += 1
            new_list.append(new_word)
            
        
        
    
    
    
    return new_list

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
   #print filename
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    data = netfile.read()		
    return data

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()
#print gen_all_strings('a') 
#print gen_all_strings('ab')   
#print gen_all_strings('def')
#print gen_all_strings('')