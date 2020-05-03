from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(ransomNote)
        for k,v in count.items():
            if magazine.count(k) < v:
                return False
        
        return True
        
        
'''        
--------------------------------------**PROBLEM STATEMENT**---------------------------------------------
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
Note:
You may assume that both strings contain only lowercase letters.
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
'''
126 / 126 test cases passed.
Status: Accepted
Runtime: 52 ms
Memory Usage: 14 MB

'''
