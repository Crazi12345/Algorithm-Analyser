from cgitb import small
import random as rand
import time
import math

from jmespath import search

def GenerateDataSet(num):
    dataset = {}
    for i in range(num):
        dataset[i]= rand.randint(1,num)
    return dataset

max = GenerateDataSet(10000)
medium = GenerateDataSet(500)
min = GenerateDataSet(25)
searchTerm = 5

times = time.perf_counter_ns
timesName = " NanoSeconds"
bigO = 50
bigODivders = [1,1.2,2,2.35,4,8,33000000]
bigOFound = 1


def printTime(time):
    if time/1000000000 < 0:
        print(str(time/1000000000)+" Seconds")
    else:
        print(str(time)+" Nanoseconds")
    
def BigOCal(method):
    first = GenerateDataSet(bigO)
    second = GenerateDataSet(bigO*2)
    start = time.perf_counter_ns()
    method(first)
    end = time.perf_counter_ns()
    timeO1 = end-start

    start = time.perf_counter_ns()
    method(second)
    end = time.perf_counter_ns()
    timeO2 = end-start

    bigOFound = 0
    bestDiff = timeO2*2
    diff = 0
    for i in range (1,len(bigODivders)):
        diff = math.sqrt((timeO1-(timeO2/bigODivders[i]))**2)
      #  print(str(i)+": "+str(diff))
        if  bestDiff>diff:
            bestDiff = diff
            bigOFound = i


    if timeO1 == timeO2:
        print("O(1)")
    elif bigOFound == 1:
        print("O(log(N))")
    elif bigOFound == 2:
        print("O(N)")    
    elif bigOFound == 3:
        print("O(N*log(N))")
    elif bigOFound == 4:
        print("O(N^2)")
    elif bigOFound == 5:
        print("O(N^3)")
    elif bigOFound == 6:
        print("O(2^N)")

    
    likelyhood = ((diff)/timeO1)*100
    print("likelyhood: "+str(likelyhood)+"%")
    print()
    print("----------------------------------------------------------------------------------------------------------------")
    print()
   
    




def TestAlgorithm(method):
    data = [min,medium,max]
    print(method.__name__+":")
    time1 = 0
    time2 = 0
    time3 = 0
    for k in range(len(data)):
        print("Output"+str(k+1)+":",end="      ")
        start = times()
        method(data[k])
        end = times()
        print(method(data[k]))
        if time1 == 0:
            time1 = (end-start)
            print("Time"+str(k+1)+":",end="      ")
            printTime(time1)
            
        elif time2 == 0:
            time2 = end -start
            print("Time"+str(k+1)+":",end="      ")
            printTime(time2)
        elif time3 == 0:
            time3 = end-start
            print("Time"+str(k+1)+":",end="      ")
            printTime(time3)
    BigOCal(method)
        

def Algorithms():
  
    TestAlgorithm(BubbleSort)
    TestAlgorithm(insertionSort)
    TestAlgorithm(TestAlg)
    
    


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
              
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
       
        array[j + 1] = key
    return array

def BubbleSort(dataset):
    length = len(dataset)
    for i in range(length):
        for j in range(length - 1):
         if dataset[j]>dataset[j+1]:
                temp = dataset[j]
                dataset[j]=dataset[j+1]
                dataset[j+1]=temp
           
    return dataset

def TestAlg(dataset):
    for i in range(len(dataset)):
        a = i+i
def __init__():
     Algorithms()

Algorithms()