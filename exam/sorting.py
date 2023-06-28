#import datastructures
from array import array
from functools import wraps
import math
import time as t
import random as rand
import sys
sys.setrecursionlimit(20000)

scale_factor = 10

smallSize = 100
mediumSize = smallSize*scale_factor
largeSize = mediumSize*scale_factor
sizes = [smallSize, mediumSize, largeSize]

smallRandomDataset = []
mediumRandomDataset = []
largeRandomDataset = []

smallOrderedDataset = []
mediumOrderedDataset = []
largeOrderedDataset = []

smallReverseOrderedDataset = []
mediumReverseOrderedDataset = []
largeReverseOrderedDataset = []

smallDuplicateDataset = []
mediumDuplicateDataset = []
largeDuplicateDataset = []

smallPatternDataset = []
mediumPatternDataset = []
largePatternDataset = []

expected_scale_factors = {
        "O(1)": 1,
        "O(log n)": math.log(scale_factor,2),
        "O(sqrt(n))": math.sqrt(scale_factor),
        "O(n)": scale_factor,
        "O(n log n)": scale_factor * math.log(scale_factor,2),
        "O(n²)": scale_factor ** 2,
        "O(n³)": scale_factor ** 3,
        "O(2^n)": 2 ** scale_factor,
        "O(n!)": math.factorial(scale_factor), 
        "O(n^n)": scale_factor ** scale_factor
        }

dataset_names = ['Random', 'Ordered', 'ReverseOrdered', 'Duplicate', 'Pattern']
datasets = {
    'Small': [smallRandomDataset, smallOrderedDataset, smallReverseOrderedDataset, smallDuplicateDataset, smallPatternDataset],
    'Medium': [mediumRandomDataset, mediumOrderedDataset, mediumReverseOrderedDataset, mediumDuplicateDataset, mediumPatternDataset],
    'Large': [largeRandomDataset, largeOrderedDataset, largeReverseOrderedDataset, largeDuplicateDataset, largePatternDataset],
    'Random': [smallRandomDataset, mediumRandomDataset, largeRandomDataset],
    'Ordered': [smallOrderedDataset, mediumOrderedDataset, largeOrderedDataset],
    'ReverseOrdered': [smallReverseOrderedDataset, mediumReverseOrderedDataset, largeReverseOrderedDataset],
    'Duplicate': [smallDuplicateDataset, mediumDuplicateDataset, largeDuplicateDataset],
    'Pattern': [smallPatternDataset, mediumPatternDataset, largePatternDataset]
}
big_o_values = {
        "O(n²)": "10"
        }
################################### Data

def generateRandomDatasets():
    for i, dataset in enumerate(datasets["Random"]):
        for _ in range(sizes[i]):
            dataset.append(rand.randint(0, sizes[i]))  

def generateOrderedDatasets():
    for i, dataset in enumerate(datasets["Ordered"]):
        dataset.extend(list(range(sizes[i])))  

def generateReverseOrderedDatasets():
    for i, dataset in enumerate(datasets["ReverseOrdered"]):
        dataset.extend(list(range(sizes[i], 0, -1)))  

def generateDuplicateDatasets():
    for i, dataset in enumerate(datasets["Duplicate"]):
        dataset.extend([0] * sizes[i])  

def generatePatternDatasets():
    pattern = [2, 1]  # define your pattern here
    for i, dataset in enumerate(datasets["Pattern"]):
        dataset.extend(pattern * (sizes[i] // len(pattern)))  

def generateAllDatasets():
    generateRandomDatasets()
    generateOrderedDatasets()
    generateReverseOrderedDatasets()
    generateDuplicateDatasets()
    generatePatternDatasets()

def printDatasets():
    for category, category_datasets in datasets.items():
        print(f"{category}:")
        for i, dataset in enumerate(category_datasets):
            print(f"  Dataset {i}: {dataset}")

    
##################### algorithms


def bubble_sort(dataset):
    numbers = dataset
    for i in range(len(numbers)):
       for j in range(len(numbers) - 1):
           if numbers[j] > numbers[j + 1]:
               numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def insertion_sort(dataset):
    numbers = dataset
    for i in range(1,len(numbers)):
        key = numbers[i]
        j = i-1
        while j>=0 and numbers[j]>key:
            numbers[j+1] = numbers[j]
            j = j-1
        numbers[j+1] = key
    return numbers


def selection_sort(dataset):
    input_list = dataset
    out_list = []
    while len(input_list) != 0:
       minimum = 0
       for j in range(len(input_list)):
           if(input_list[j]< input_list[minimum]):
                minimum = j
       out_list.append(input_list.pop(minimum))
    #print(out_list)
    return out_list

def merge(ds1,ds2):
    out_list = []
    ds1_n = len(ds1)
    ds2_n = len(ds2)
    i = 0
    j = 0
    while i<ds1_n and j<ds2_n:
        if ds1[i]<ds2[j]:
            out_list.append(ds1[i])
            i+=1
        else:
            out_list.append(ds2[j])
            j+=1

    while i<ds1_n:
        out_list.append(ds1[i])
        i+=1


    while j<ds2_n:
        out_list.append(ds2[j])
        j+=1

    return out_list

def mergesort(dataset):
    if len(dataset) <= 1:
        return dataset
    r = len(dataset)//2
    l = dataset[:r]
    m = dataset[r:]
    
    l= mergesort(l)
    m = mergesort(m)
    output = merge(l,m)
    return output
def counting_sort(dataset):

    # Find maximum value in dataset to define the size of the count array
    max_val = max(dataset)
    
    # Create a count array and output array
    count = [0] * (max_val + 1)
    output = [0] * len(dataset)

    # Count the occurrence of each number in the dataset
    for num in dataset:
        count[num] += 1

    # Modify the count array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Fill the output array
    for i in range(len(dataset) - 1, -1, -1):
        output[count[dataset[i]] - 1] = dataset[i]
        count[dataset[i]] -= 1

    return output


def partition(array, low, high):

  pivot = array[high]

  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1

      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quick_sort(array, low, high):
  if low < high:

    pi = partition(array, low, high)

    quick_sort(array, low, pi - 1)

    quick_sort(array, pi + 1, high)

def call_quick_sort(dataset):
    data = dataset 
    size = len(data)
    quick_sort(data,0,size-1)
    return data
def heapify(arr, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
  
def heap_sort(dataset):
      arr = dataset
      n = len(arr)
  
      for i in range(n//2, -1, -1):
          heapify(arr, n, i)
  
      for i in range(n-1, 0, -1):
          arr[i], arr[0] = arr[0], arr[i]
  
          heapify(arr, i, 0)
      return arr
###### List of algorithms
algorithms = {
  #  'Bubble Sort': {
  #      'function': bubble_sort,
  #      'worst_case': 'O(n^2)'
  #  },
  #  'Insertion Sort': {
  #      'function': insertion_sort,
  #      'worst_case': 'O(n^2)'
  #  },
    #'Selection Sort': {
    #        'function': selection_sort,
     #       'worst_case': 'O(n²)'
      #  },
    'Merge Sort': {
            'function': mergesort,
            'worst_case': 'O(n log(n))'
        },
    'counting_sort':{
        'function': counting_sort,
        'worst_case': 'O(n+k)'
        },
    'Heap Sort':{
        'function': heap_sort,
        'worst_case':'O(somethonh)'
        },
    'Quick Sort':{
        'function':call_quick_sort,
        'worst_case': 'O(n^2)'
        }
}


############################### BIG O        

def approximate_big_o(scale_factor, time_small, time_medium, time_large):
    # Calculate the observed scale factor
    scale_factor_medium = time_medium / time_small
    scale_factor_large = time_large / time_medium
    avg_scale_factor_observed = (scale_factor_medium + scale_factor_large) / 2

    # Calculate the expected scale factors for different time complexities

    # Find the time complexity that gives the expected scale factor closest to the observed scale factor
    best_fit = min(expected_scale_factors.keys(), key=lambda complexity: abs(avg_scale_factor_observed - expected_scale_factors[complexity]))

    return best_fit

def big_O(times):
    time_small, time_medium, time_large = times
    big_o = approximate_big_o(scale_factor, time_small, time_medium, time_large)
    return big_o


###################################### Tester
def testAlgorithms():
   for algorithm_name, algorithm in algorithms.items():
      print()
      print()
      print(algorithm_name+":")
      for dataset_name, dataset_list in datasets.items():
            print(" "+dataset_name+":")
            times = []
            for i, dataset in enumerate(dataset_list):
                dataset_cp = dataset.copy()
                start = t.perf_counter_ns() 
                sorted_numbers = algorithm['function'](dataset_cp)
                end = t.perf_counter_ns()  
                if sorted(dataset.copy()) != sorted_numbers:
                    print("         ERROR: NOT CORRECTLY SORTED")
                    continue
                time_taken = (end-start)/1000000
                if len(dataset_list)>4:
                    print("   " + dataset_names[i] + " Dataset:")
                else:
                        times.append(time_taken)
                print("     time_ms: "+str(time_taken))
                print()
            if len(times)>2:
                big_o = big_O(times)
                print("     Approximated Big O: " + big_o)

################################## Program
generateAllDatasets()
testAlgorithms()
