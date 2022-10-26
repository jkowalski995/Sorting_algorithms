'''
This is a Python implementation of Bubble Sort algorithm.
Creator: Jakub Kowalski
Country: Poland
'''

from random import randint
import time

random_len = randint(0, 100)
data = [randint(0, 1000) for _ in range(random_len)]

def swap_data(data, i):
    tmp_val = data[i + 1]
    data[i + 1] = data[i]
    data[i] = tmp_val
    return data

def bubble_sort(data):
    start_time = time.time()
    should_keep_sorting = True

    while should_keep_sorting:
        
        should_keep_sorting = False
        
        for i in range(len(data) - 1):

            if data[i] > data[i + 1]:
                data = swap_data(data, i)
                should_keep_sorting = True
        
    print(f' --- SORTING COMPLETE ---\nSorted data: {data}')
    print(f' --- Time of execution ---\n{time.time() - start_time} seconds')
    return data

bubble_sort(data)


