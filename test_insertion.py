# 1. Unsorted int numbers
# 2. Unsorted float numbers
# 3. Unsorted strings
# 4. Sorted numbers
# 5. Sorted strings
# 6. Empty data
# 7. Data with one element

from unittest import result
import pytest

from Insertion_sort.insertion import insertion_sort, insert_values

class TestInsertionSort():

    def test_unsorted_int_numbers(self):
        data = [78,56,22,3,1,2,8,4]
        result = insertion_sort(data)
        assert [1, 2, 3, 4, 8, 22, 56, 78], result

    def test_unsorted_float_numbers(self):
        data = [-78,56.1,-22,3.5,1,-2.2,8,4]
        result = insertion_sort(data)
        assert [-78, -22, -2.2, 1, 3.5, 4, 8, 56.1], result

    def test_unsorted_strings(self):
        data = ['ac', 'db', 'a','aw','zx', 'u','w']
        result = insertion_sort(data)
        assert ['a', 'ac', 'aw', 'db', 'u', 'w', 'zx'], result

    def test_sorted_numbers(self):
        data = [1, 2, 3, 4, 8, 22, 56, 78]
        result = insertion_sort(data)
        assert [1, 2, 3, 4, 8, 22, 56, 78], result

    def test_sorted_strings(self):
        data = ['a', 'ac', 'aw', 'db', 'u', 'w', 'zx']
        result = insertion_sort(data)
        assert ['a', 'ac', 'aw', 'db', 'u', 'w', 'zx'], result

    def test_empty_data(self):
        data = []
        result = insertion_sort(data)
        print(result)
        assert result == []

    def test_one_element(self):
        data = ['a']
        result = insertion_sort(data)
        assert ['a'], result

# 1. Data and res but j=0
# 2. Data and res but j>0
# 3. Data = None and res but j=0
# 4. Data = None and res but j=1
# 5. Data and res = [] but j=0
# 6. Data and res = [] but j>0

class TestInsertValues():

    def test_data_res_j0(self):
        data = 22
        j = 0
        res = [23, 44]
        result = insert_values(data, res, j)
        assert [22, 23, 44], result

    def test_data_res_j1(self):
        data = 31
        j = 1
        res = [23, 44]
        result = insert_values(data, res, j)
        assert [23, 31, 44], result

    def test_data_none_j0(self):
        data = None
        j = 0
        res = [23, 44]
        result = insert_values(data, res, j)
        assert [23, 44], result

    def test_data_none_j1(self):
        data = None
        j = 1
        res = [23, 44]
        result = insert_values(data, res, j)
        assert [23, 44], result

    def test_res_empty_j0(self):
        data = 22
        j = 0
        res = []
        result = insert_values(data, res, j)
        assert [22], result

    def test_res_empty_j1(self):
        data = 22
        j = 1
        res = []
        result = insert_values(data, res, j)
        assert [22], result
