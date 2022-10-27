'''
This is a Python implementation of Insertion Sort algorithm.
Creator: Jakub Kowalski
Country: Poland
'''

def insert_values(data, res, j):
    if j == 0:
        res = [data] + res
    else:
        res = res[:j] + [data] + res[j:]
    return res

def insertion_sort(data):
    res = []
    for i in range(0,len(data)):
        for j in range(len(res)):
            if data[i] <= res[j]:
                res = insert_values(data[i], res, j)
                break
            elif j == (len(res)-1):
                res.append(data[i])
    return res
