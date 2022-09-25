from array import array
import numpy as np
 
a = np.array([1,2,3,4])

def print_array(arr):
    for value in arr:
        print(value)

def sum_array(arr):
    return arr.sum()

print(sum_array(a))

def mult_array(arr):
    return map(lambda x: x*3, arr)

print_array(mult_array(a))

