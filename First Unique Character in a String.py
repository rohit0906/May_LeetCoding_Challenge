from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        #print(count)
        change=False
        if len(s)==1: return 0
        cur=len(s)
        for k,v in count.items():
            if v==1:
                if cur>s.index(k):
                    cur=s.index(k)
                    change=True
                    
        if change==False:return -1
        
        return cur
        
        
        
        
'''
------------------------------------------**PROBLEM STATEMENT**-------------------------------------------
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
'''
104 / 104 test cases passed.
Status: Accepted
Runtime: 56 ms
Memory Usage: 13.7 MB
'''
