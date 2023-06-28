
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.append(item)

    def addFront(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
            
    def is_empty(self):
        return len(self.stack) == 0



def max_heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)

    # Start from the last non-leaf node
    start_index = n // 2 - 1

    # Perform max heapify operation for all nodes from last non-leaf node to root
    for i in range(start_index, -1, -1):
        max_heapify(arr, n, i)

def min_heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < n and arr[i] > arr[l]:
        smallest = l
    
    if r < n and arr[smallest] > arr[r]:
        smallest = r
    
    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        min_heapify(arr, n, smallest)

def build_min_heap(arr):
    n = len(arr)

    # Start from the last non-leaf node
    start_index = n // 2 - 1

    # Perform min heapify operation for all nodes from last non-leaf node to root
    for i in range(start_index, -1, -1):
        min_heapify(arr, n, i)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size//2)-1, -1, -1):
            min_heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
        
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)
    
    for i in range((len(array)//2)-1, -1, -1):
        min_heapify(array, len(array), i)

arr = [2,4,3,7,7,5,6,8,9]
arr_max = arr.copy()
arr_min = arr.copy()
build_max_heap(arr_max)
print("max:"+str(arr_max))
deleteNode(arr_max,min(arr_max))
print("max:"+str(arr_max))
insert(arr_max,1)
print("max:"+str(arr_max))
build_min_heap(arr_min)
print("min:"+str(arr_min))
deleteNode(arr_min,min(arr_min))
print("min:"+str(arr_min))
insert(arr_min,1)
print("min:"+str(arr_min))
