'''
This is a Python implementation of Bubble Sort algorithm.
Creator: Jakub Kowalski
Country: Poland
'''

from random import randint
import time
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%d/%m/%Y %I:%M:%S %p')

unsorted_lst = []
random_len = randint(0, 100)
for i in range(random_len):
    unsorted_lst.append(randint(0, 1000))


def bubble_sort(unsorted_lst):
    logging.info(' --- STARTING THE BUBBLE SORT ALGORITHM ---')
    logging.info(f' LOADED LIST: {unsorted_lst}')

    sort_flag = 1
    while sort_flag != 0:
        sort_flag = 0
        for i in range(len(unsorted_lst),1,-1):
            if unsorted_lst[i - 1] < unsorted_lst[i - 2]:
                logging.info(f' Found unsorted pair: {unsorted_lst[i-1], unsorted_lst[i-2]}')
                logging.info(' --- SORTING ---')
                tmp_val = unsorted_lst[i - 1]
                unsorted_lst[i - 1] = unsorted_lst[i - 2]
                unsorted_lst[i - 2] = tmp_val
                logging.info(f' List after sorting: {unsorted_lst}')
                sort_flag = 1
        
    sorted_lst = unsorted_lst
    logging.info(f' --- SORTING COMPLETE ---\nSorted list: {sorted_lst}')

start_time = time.time()
bubble_sort(unsorted_lst)
logging.info(f' --- Time of execution ---\n{time.time() - start_time} seconds')
