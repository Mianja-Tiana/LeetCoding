"""
"""
class LeetCode:

#Palindrome Number : https://leetcode.com/problems/palindrome-number/description/
    def isPalindrome(self, x):
            """
            :type x: int
            :rtype: bool
            """
            x_str = str(x)
            return x_str == x_str[::-1]
    
# Two Sum Problem :https://leetcode.com/problems/two-sum/
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i , num1 in enumerate (nums):
            for j ,num2 in enumerate (nums):
                if i != j and num1 + num2 == target:
                    return [i, j]
                
# Roman to Integer : https://leetcode.com/problems/roman-to-integer/
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
}

        total = 0
        prev_value =0
        for char in reversed(s):
            current = roman[char]
            if current < prev_value:
                total -= current
            else :
                total += current
            prev_value = current
        return total