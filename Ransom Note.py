class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if not i in magazine:
                return False
            magazine=magazine.replace(i,"",1)
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
Runtime: 40 ms
Memory Usage: 13.8 MB
'''
