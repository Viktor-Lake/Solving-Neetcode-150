"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = defaultdict(int)
        for element in s:
            frequency[element] += 1
        for element in t:
            frequency[element] -= 1
        for key in frequency:
            if frequency[key] != 0:
                return False
        return True

#O(n) in time