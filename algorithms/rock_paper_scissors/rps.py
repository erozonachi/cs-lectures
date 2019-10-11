#!/usr/bin/python

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
