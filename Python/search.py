import time


array = [12,23,45,9,0,34,1,2,4,5,73,31,8,3]


def linSearch(array, target):
    for i in range(0,len(array)):
        if array[i]==target:
            return i


def binarySearch(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)
        else:
            return binarySearch(array, x, mid + 1, high)
    else:
        return -1



array = sorted(array)
start = time.time()
result = binarySearch(array, 73, 0, len(array)-1)
end = time.time()
time_taken = end-start
print(time_taken)
print()
start = time.time()
result  = linSearch(array,73)
end = time.time()
time_taken = end-start
print(time_taken)
print()
