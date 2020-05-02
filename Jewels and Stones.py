class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for i in S:
            if i in J:
                count=count+1
            
    
        return count
    
'''
Running status
Test passed 254/254
Runtime: 20 ms
Memory Usage: 13.8 MB
'''
