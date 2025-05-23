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