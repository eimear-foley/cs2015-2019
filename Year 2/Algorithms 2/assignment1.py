# CS2516 - Algorithms & Data Structures II
# Assignment 1

import random

### Merge Sort
def mergeSort(lst):
    n = len(lst)
    if n > 1:
        list1 = lst[:n//2]
        list2 = lst[n//2:]
        mergesort(list1)
        mergesort(list2)
        merge(list1, list2, lst)
    return lst

def merge(list1, list2, lst):
    f1 = 0
    f2 = 0
    while f1 + f2 < len(lst):
        if f1 == len(list1):
            lst[f1+f2] = list2[f2]
            f2 += 1
        elif f2 == len(list2):
            lst[f1+f2] = list1[f1]
            f1 += 1
        elif list2[f2] < list1[f1]:
            lst[f1+f2] = list2[f2]
            f2 += 1
        else:
            lst[f1+f2] = list1[f1]
            f1 += 1

### In-Place Quick Sort
def quickSort(lst):
    n = len(lst)
    for i in range(len(lst)):
        j = random.randint(0, n-1)
        (lst[i], lst[j]) = (lst[j], lst[i])
    _quicksort(lst, 0, n-1)
    return lst

def _quicksort(lst, first, last):
    #sort elements of lst from first up to last
    if last > first:
        pivot = lst[first]
        f = first + 1
        b = last
        while f <= b:
            while f <= b and lst[f] <= pivot:
                f += 1
            while f <= b and lst[b] >= pivot:
                b -= 1
            if f < b:
                (lst[f], lst[b]) = (lst[b], lst[f])
                f += 1
                b -= 1
        (lst[b], lst[first]) = (lst[first], lst[b])
        _quicksort(lst, first, b-1)
        _quicksort(lst, b+1, last)

import re

def wordbst(filename):
    """ Return a list containing the words in file 'filename'. """
    file = open(filename, "r")  #open the file
    fulltext = file.read()         #read it all into one big string
    stripped = re.sub("[^a-zA-Z\s]+", "", fulltext)  #remove non-letters or -spaces
    wordlist = stripped.split() #split the string on white space into words in a list
    print(len(wordlist), "words in total")
    return wordlist
