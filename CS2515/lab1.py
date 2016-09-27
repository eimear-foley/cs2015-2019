from time import perf_counter
import random

def replaceMethod(lst1, lst2):

    if len(lst1) != len(lst2):
        return False
    
    i = 0
    for j in lst1:
        found = False
        while i < len(lst2) and not found:
            if j == lst2[i]:
                j = None
                found = True
            else:
                found = False
                i += 1
    return found

def sortMethod(lst1, lst2):

    if len(lst1) != len(lst2):
        return False

    lst1.sort()
    lst2.sort()

    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True

def makeTable():

    table = []
    for i in range(10000):
        table += [0]
    return table

def countMethod(lst1,lst2):

    if len(lst1) != len(lst2):
        return False

    table = makeTable()
    
    for i in range(len(lst1)):
        table[lst1[i]] += 1
        table[lst2[i]] -= 1
    for n in range(10000):
        if table[n] != 0:
            return False
    return True

def performanceCheck(lst1,lst2):

    print('Length of list 1: %i' %(len(lst1)))
    print('Length of list 2: %i' %(len(lst2)))

    before_time = perf_counter()
    replace = replaceMethod(lst1,lst2)
    after_time = perf_counter()
    print('Replace Method: %f seconds' % (after_time - before_time))

    before_time = perf_counter()
    sort = sortMethod(lst1,lst2)
    after_time = perf_counter()
    print('Sort Method: %f seconds' % (after_time - before_time))

    if len(lst1) < 100000:
        before_time = perf_counter()
        count = countMethod(lst1,lst2)
        after_time = perf_counter()
        print('Count Method: %f seconds' % (after_time - before_time))

def randomListsCheck(n):

    lst = []
    for i in range(n):
        lst += [random.randint(0,n)]

    random_copy = lst.copy()   
    performanceCheck(lst, random_copy)

def countDict(lst1,lst2):

    d = {n : 0 for n in range(10000)}
    
