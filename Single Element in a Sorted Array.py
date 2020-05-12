'''
-----------------------------------*****PROBLEM STATEMENT******-----------------------------------------
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space.
'''

'''
O(n) solution:-

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=nums[0]
        for i in range(1,len(nums),2):
            if n == nums[i] and nums[1]!=nums[i+1]:
                n=nums[i+1]
            elif n!=nums[i]:
                break
        
        return n
            

'''

'''
O(logn) solution:-

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while True:
            mid = (low + high) // 2
            if mid % 2 == 1:
                mid -= 1
            if mid < high and nums[mid] == nums[mid+1]:
                low = mid + 2
            elif mid > low and nums[mid] == nums[mid-1]:
                high = mid - 2
            else:
                return nums[mid]
                
'''
