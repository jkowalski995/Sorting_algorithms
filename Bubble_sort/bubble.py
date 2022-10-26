'''
This is a Python implementation of Bubble Sort algorithm.
Creator: Jakub Kowalski
Country: Poland
'''

def swap_data(data, i, j):
    data[i], data[j] = data[j], data[i]

def bubble_sort(data):
 
    should_keep_sorting = True

    while should_keep_sorting:
        
        should_keep_sorting = False
        
        for i in range(len(data) - 1):

            if data[i] > data[i + 1]:
                swap_data(data, i, i + 1)
                should_keep_sorting = True
        
    print(f' --- SORTING COMPLETE ---\nSorted data: {data}')
    return data