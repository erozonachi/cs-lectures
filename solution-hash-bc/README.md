# Sprint-Challenge-Solution--Hash-Python

## Interview Questions
Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
* What is the worse case scenario if you try to extend the storage size of a dynamic array?

Storing a sequence of elements.
Each element is the same data type.
Occupies a contiguous block of memory.
Functionality to increase or decrease size of array - at a cost.
Can access access data in constant time with this equation: memory_address = starting_address + index * data_size.
Access O(1), add or remove from front O(n), add or remove from back O(1).
Worse case scenario is that there is not room, so a new array must be created and all elements copied over at O(n).

Explain how a blockchain is structured. What are the blocks, what are the chain? How is the data organized?
  * Blocks are data objects similar nodes in a linked list
  * Blocks contain an index, list of transactions, timestamp, proof, and cryptographic hash of previous block
  * The chain is formed because each block has the cryptographic hash of the previous block.
  * Can't change one without changing all following
  * Proof is included to later validate that a valid proof was used to mine the block

Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
  * Arbitrarily hard problem to solve
  * Can't be done cleverly, just by brute force consumption of computation
  * This work is distributed across all the miners, so what would take one computer years to solve is solved in 10 minutes by the group
  * This protects the chain because one bad actor can never outperform the rest of the miners if they change a transaction and try to re-mine blocks
  * An attacker who gains 51% of mining power can take over.  This is a real risk with most mining being done by large pools
  
