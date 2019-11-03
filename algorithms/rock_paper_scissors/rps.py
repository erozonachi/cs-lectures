""" #!/usr/bin/python

import sys

# given n
# for card in cards:
# for i in n:
# if i == 0:
# first have => [card * n]
# continue
# => [ card * (n - i), (card+1) * i ]


def rps(n, word, list_of_words):
    # push word to the list
    list_of_words.append(word)
    # if n == 1 - return a list with the list of everything
    if n == 1:
        return [list_of_words]
    # otherwise call itself 3 times with n - 1, rps and pass copied list
    l1 = rps(n - 1, "rock", list_of_words[:])
    l2 = rps(n - 1, "paper", list_of_words[:])
    l3 = rps(n - 1, "scissors", list_of_words[:])
    # add returned lists to a list and return it
    l = l1
    l.extend(l2)
    l.extend(l3)

    return l


def rock_paper_scissors(n):
    pass
    if n == 0:
        return [[]]

    l1 = rps(n, "rock", [])
    l2 = rps(n, "paper", [])
    l3 = rps(n, "scissors", [])

    l = l1
    l.extend(l2)
    l.extend(l3)

    return l


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

# print(rock_paper_scissors(2))
 """
"""
   #!/bin/python3

   import math
   import os
   import random
   import re
   import sys
   from collections import deque

   # HashTable Class


   class HashTable:
       def __init__(self, size):
           self.storage = [[] for i in range(size-1)]

       def hashFunc(self, val):
           if val > 0:
               return val - 1

       def insertVal(self, obj):
           if self.hashFunc(obj['value']) < len(self.storage):
               self.storage[self.hashFunc(obj['value'])].append(obj)

       def getVal(self, val):
           if self.storage[self.hashFunc(val)] and len(self.storage[self.hashFunc(val)]) > 0:
               return self.storage[self.hashFunc(val)].pop(0)
           return None


   # A helper recursive function
   result = []


   def flavorsRecursive(store, money, control, cache):
       global result
       if control == 0:
           if len(cache) == 2:
               result[:] = cache
               return result

       for i in range(1, money):
           print(i)
           temp = store.getVal(i)
           if len(cache) == 2:
               val_a = cache[0]
               val_b = cache[1]
               if temp != None and money == val_a['value'] + temp['value']:
                   cache[1] = temp
                   print(cache)
                   result[:] = cache
                   flavorsRecursive(store, money, money -
                                    val_a['value'] + temp['value'], cache)
               elif temp != None and money == val_b['value'] + temp['value']:
                   cache.pop(0)
                   cache[1] = temp
                   print(cache)
                   result[:] = cache
                   flavorsRecursive(store, money, money -
                                    val_b['value'] + temp['value'], cache)
           elif temp != None and control - temp['value'] >= 0:
               cache.append(temp)
               val1 = cache[0]
               print(val1)
               print(cache)
               flavorsRecursive(store, money, control - temp['value'], cache)
       return result
   # Complete the whatFlavors function below.


   def whatFlavors(cost, money):
       #choice1 = None
       #choice2 = None
       #val = None
       hashStore = HashTable(money)
       for i in range(len(cost)):
           if cost[i] < money:
               hashStore.insertVal({'id': i, 'value': cost[i]})
           '''count = cost.count(money - cost[i])
           if count == 2 or ((count) == 1 and cost.index(money - cost[i]) != i):
               choice1 = i
               val = cost[i]
               break'''
       #cost[choice1] = 0
       #choice2 = cost.index(money - val)
       choices = flavorsRecursive(hashStore, money, money, [])
       print(choices)
       if len(choices) >= 2:
           choice1 = choices[0]
           choice2 = choices[1]

           print(f"{choice1['id'] + 1} {choice2['id'] + 1}")


   #whatFlavors([1, 4, 5, 3, 2], 4)
   #whatFlavors([2, 2, 4, 3], 4)
   whatFlavors([7, 2, 5, 4, 11], 12)
   """


def duplicates(arr, offset):
    dups = 1
    if offset >= len(arr)-1 or arr[offset] != arr[offset+1]:
        return dups

    for i in range(offset, len(arr)):
        if i < len(arr)-1 and arr[i] == arr[i+1]:
            dups += 1
        else:
            break

    return dups

# Complete the countTriplets function below.


def countTriplets(arr, r):
    arr.sort()
    pos1 = 1
    pos2 = 1
    pos3 = 1
    i = 0
    count = 0

    while i < len(arr)-3:
        if r > 1:
            pos1 = duplicates(arr, i)
            pos2 = duplicates(arr, i+pos1)
            pos3 = duplicates(arr, i+pos1+pos2)

        if arr[i]*r == arr[i+pos1] and arr[i+pos1]*r == arr[i+pos1+pos2]:
            count += (pos1 * pos2 * pos3)

        i += pos1

    return count


print(countTriplets([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))
