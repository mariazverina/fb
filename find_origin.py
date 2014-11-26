'''
Created on 25 Nov 2014

@author: mariaz
'''
import unittest

def _find_origin(arr, i, j):
    # BUG-3 - short array edge case
    if j-i < 2:
        return j

    mid = (i + j) / 2   # don't need to do "C style" i + (j - i) / 2 as Python has no integer overflow    
    if arr[mid] > arr[0] and arr[mid+1] < arr[-1]:
        return mid + 1
    
    if arr[mid] > arr[0]:
        return _find_origin(arr,mid,j)
    
    if arr[mid] < arr[-1]:
        return _find_origin(arr,i,mid)
    
    raise ValueError("Unexpected input :" + repr(arr))


def find_origin(arr):
    # BUG-1: need to handle already sorted inputs
    if arr[0] < arr[-1]:    
        return 0
    
    # BUG-2: need to handle case where list repetition occurs in first/last element
    if arr[0] == arr[-1] and len(arr) > 1:   
        for i,n in enumerate(arr):
            if n != arr[0]:
                return i + find_origin(arr[i:])
        return None
        
    return _find_origin(arr, 0, len(arr)-1)

class Test(unittest.TestCase):

    def testSimpleCase(self):
        arr = [22,25,29,32,39,44,59,1,6,12]
        self.assertEqual(7, find_origin(arr))
    
    def testSingleElementCase(self):
        arr = [22]
        self.assertEqual(0, find_origin(arr))
    
    def testTwoElementCase(self):
        arr = [2,1]
        self.assertEqual(1, find_origin(arr))

    def testTwoElementSortedCase(self):
        arr = [1,2]
        self.assertEqual(0, find_origin(arr))

    def testRepetitionsCase(self):
        arr = [22,25,29,32,32,32,32,39,44,59,1,6,12]
        self.assertEqual(10, find_origin(arr))
    
    def testDegenerateCase(self):
        arr = [2,2,2,2,2,1,2]
        self.assertEqual(5, find_origin(arr))

    def testDegenerateCaseIncreasing(self):
        arr = [2,2,2,2,2,3,1,2]
        self.assertEqual(6, find_origin(arr))

    def testAlreadySortedCase(self):
        arr = range(25)
        self.assertEqual(0, find_origin(arr))

    def testAllSameCase(self):
        arr = [2,2,2,2,2,2]
        self.assertEqual(None, find_origin(arr))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDegenerateCase']
    unittest.main()