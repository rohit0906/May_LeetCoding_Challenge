class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (num**(0.5)).is_integer()
'''        
-----------------------------------------------***PROBLEM Statement**-------------------------------------------


Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''



'''

68 / 68 test cases passed.
Status: Accepted
Runtime: 24 ms
Memory Usage: 14 MB
'''
