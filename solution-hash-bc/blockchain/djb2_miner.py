# Experiment, does not work

import hashlib
import requests

import sys

from uuid import uuid4

import random

chars = 'abcdefghijklmnopqrstuvwxyz'
# get_random_string(50, chars)


def random_string(length):
    return ''.join(random.choice(chars) for i in range(length))


def hash(string):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)

    return hash % 10


def proof_of_work(last_proof):
    """
    Simple Proof of Work Algorithm
    - Find a number p' such that hash(pp') contains 6 leading
    zeroes, where p is the previous p'
    - p is the previous proof, and p' is the new proof
    """

    print("Searching for next proof")
    proof = random_string(6)
    last_hash = hash(last_proof)
    while valid_proof(last_hash, proof) is False:
        proof = random_string(6)

    print("Proof found: " + str(proof))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Does the new proof collide with the old proof
    using the djb2 hashing algorithm?
    """
    double_proof = proof + proof
    hashed_proof = hash(double_proof)

    print(hashed_proof)
    print(last_hash)

    return hashed_proof == last_hash


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = int(sys.argv[1])
    else:
        node = "http://localhost:5000"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "w+")
    id = f.read()
    if len(id) == 0:
        # Generate a globally unique ID
        id = str(uuid4()).replace('-', '')
        print("Created new ID: " + id)
        f.write(id)
    f.close()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        # r = requests.get(url=node + "/last_proof")
        # data = r.json()
        new_proof = proof_of_work('aaaaaa')

        # post_data = {"proof": new_proof,
        #              "id": id}

        # r = requests.post(url=node + "/mine", json=post_data)
        # data = r.json()
        # if data.get('message') == 'New Block Forged':
        #     coins_mined += 1
        #     print("Total coins mined: " + str(coins_mined))
        # else:
        #     print(data.get('message'))
