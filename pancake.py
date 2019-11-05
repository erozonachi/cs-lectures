def flip(arr, k):
    leftIdx = 0
    rightIdx = k-1
    while leftIdx < rightIdx:
        leftVal = arr[leftIdx]
        arr[leftIdx] = arr[rightIdx]
        arr[rightIdx] = leftVal
        leftIdx += 1
        rightIdx -= 1


def pancake_sort(arr):
    # pass # your code goes here
    n = len(arr)-1
    for i in range(n, -1, -1)
    maxIndex = findMaxIndex(arr, i)
    flip(arr, maxIndex)
    flip(arr, i)
    # will that sort the whole array?


def findMaxIndex(arr, i):
    for j
    maxIndex = 0
    rturn maxIndex


arr = [1, 5, 4, 3, 2]

flip(arr, k=3)
arr = [4, 5, 1, 3, 2]

left = 0
right = k-1 = >2

left  right
[1, 5, 4, 3, 2]

4 5 1 3 2
left += 1
right -= 1
