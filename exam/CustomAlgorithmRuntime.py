import math
import time as t
        # Store the key-value pair in the dictionary

n = 1 
scale_factor = 10  #only tested on scale_factor 10
preciseness = 1000
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





def approximate_big_o(observed_times):
    # Calculate the observed scale factor
     # Calculate the expected scale factors for different time complexities
    scale_factors = [observed_times[i+1] / observed_times[i] for i in range(len(observed_times)-1)]
    
    # Calculate the average observed scale factor
    avg_scale_factor_observed = sum(scale_factors) / len(scale_factors)

    # Find the time complexity that gives the expected scale factor closest to the observed scale factor
    best_fit = min(expected_scale_factors.keys(), key=lambda complexity: abs(avg_scale_factor_observed - expected_scale_factors[complexity]))

    return best_fit

def big_O(times):
    big_o = approximate_big_o(times)
    return big_o

def dummyAlg(n):
    i = n
    s= 0
    while i>=s:
        for j in range(i,i*2):
            s=s+1
        i = int(i/2)
def  testAlgorithms():
            times = []
            global n
            for i in range(preciseness):
                start = t.perf_counter_ns() 
                dummyAlg(n)
                end = t.perf_counter_ns()  
                time_taken = (end-start)/1000000
                times.append(time_taken)
                n *=scale_factor
                print("     time_ms: "+str(time_taken))
                print()
            big_o = big_O(times)
            print("     Approximated Big O: " + big_o)



testAlgorithms()
