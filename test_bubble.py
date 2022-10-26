# 1. Unsorted int numbers
# 2. Unsorted float numbers
# 3. Unsorted strings
# 4. Sorted numbers
# 5. Sorted strings
# 6. Empty data
# 7. Data with one element

from unittest import result
import pytest

from Bubble_sort.bubble import bubble_sort

class TestBubbleSort():

    def test_unsorted_int_numbers(self):
        data = [78,56,22,3,1,2,8,4]
        result = bubble_sort(data)
        assert result == [1, 2, 3, 4, 8, 22, 56, 78]

    def test_unsorted_float_numbers(self):
        data = [-78,56.1,-22,3.5,1,-2.2,8,4]
        result = bubble_sort(data)
        assert result == [-78, -22, -2.2, 1, 3.5, 4, 8, 56.1]

    def test_unsorted_strings(self):
        data = ['ac', 'db', 'a','aw','zx', 'u','w']
        result = bubble_sort(data)
        assert result == ['a', 'ac', 'aw', 'db', 'u', 'w', 'zx']

    def test_sorted_numbers(self):
        data = [1, 2, 3, 4, 8, 22, 56, 78]
        result = bubble_sort(data)
        assert result == [1, 2, 3, 4, 8, 22, 56, 78]

    def test_sorted_strings(self):
        data = ['a', 'ac', 'aw', 'db', 'u', 'w', 'zx']
        result = bubble_sort(data)
        assert result == ['a', 'ac', 'aw', 'db', 'u', 'w', 'zx']

    def test_empty_data(self):
        data = []
        result = bubble_sort(data)
        assert result == []

    def test_one_element(self):
        data = ['a']
        result = bubble_sort(data)
        assert result == ['a']
    