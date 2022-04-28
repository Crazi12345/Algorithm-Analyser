from cgitb import small
import random as rand
import time
import math

def GenerateDataSet(num):
    dataset = {}
    for i in range(num):
        dataset[i]= rand.randint(1,num)
    return dataset

max = GenerateDataSet(10000)
medium = GenerateDataSet(50)
min = GenerateDataSet(25)
times = time.perf_counter_ns
timesName = " NanoSeconds"
bigO = 25
bigODivders = [1,1.2,2,2.3,4,8,33000000]
bigOFound = 1
def BigOCal(method):
    start = time.perf_counter_ns()
    method(GenerateDataSet(bigO))
    end = time.perf_counter_ns()
    timeO1 = end-start
    start = time.perf_counter_ns()
    method(GenerateDataSet(bigO*2))
    end = time.perf_counter_ns()
    timeO2 = end-start
    bigOFound = 1
    bestDiff = math.sqrt((timeO1-(math.sqrt((timeO2/bigODivders[4])**2)))**2)
    for i in range (1,len(bigODivders)):
        diff = timeO1-(math.sqrt((timeO2/bigODivders[i])**2))
        print(str(i)+": "+str(diff))
        if  bestDiff>math.sqrt((timeO1-(math.sqrt((timeO2/bigODivders[i])**2)))**2):
            bestDiff =math.sqrt((timeO1-(math.sqrt((timeO2/bigODivders[i])**2)))**2)
            bigOFound = i
    if bigOFound == 0:
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

    likelyhood = ((timeO2/bigODivders[bigOFound])/timeO1)*100
    print(str(likelyhood)+"%")
   
    




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
            print(str(time1)+timesName)
            
        elif time2 == 0:
            time2 = end -start
            print("Time"+str(k+1)+":",end="      ")
            print(str(time2)+timesName)
        elif time3 == 0:
            time3 = end-start
            print("Time"+str(k+1)+":",end="      ")
            print(str(time3)+timesName)
    BigOCal(method)
        

def Algorithms():
  
    TestAlgorithm(BubbleSort)
    TestAlgorithm(insertionSort)
    
    

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


def __init__():
     Algorithms()

Algorithms()