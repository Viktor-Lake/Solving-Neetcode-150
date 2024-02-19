"""
Question
Given an integer array "nums", return "true" if any value appears at least twice in the array, 
and return "false" if every element is distinct.
Constraints:

    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for element in nums:
            if element not in dictionary:
                dictionary[element] = 1
            else:
                return True
        return False