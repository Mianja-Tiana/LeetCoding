"""
"""


class ListNode(object):
     
    def __init__(self, val= 0, next=None):
         self.val = val
         self.next = next

    @staticmethod
    def from_list(input_list):
        if len(input_list)==0:
            return None

        first = ListNode(val = input_list[0])
        current = first 

        for i in range(1,len(input_list)):
            current.next= ListNode(val = input_list[i])
            current = current.next
        return first
    
    def __str__(self):
        output = "["
        current = self
        while current :
            output+=str(current.val)
            output +=","
            current = current.next
        output += ']'
        return output


class LeetCode:

#Palindrome Number : https://leetcode.com/problems/palindrome-number/description/

    def isPalindrome_slicing(self, x:int)->bool:
            
            """
            Checks if the input number is a palindrome.
            (A numeric palindrome is a number that remains the same when its digits are reversed.)

            Args:
                 x (int): An integer number.

            Returns:
                 bool: True if the number is a palindrome, False otherwise.
            """

            #Using slicing
            x_str = str(x)
            return x_str == x_str[::-1]
    
    def isPalindrome_loop(self, x:int)->bool:
            
            """
            Checks if the input number is a palindrome.
            (A numeric palindrome is a number that remains the same when its digits are reversed.)

            Args:
                 x (int): An integer number.

            Returns:
                 bool: True if the number is a palindrome, False otherwise.
            """

            # Without slicing
            x_str = str(x)
            n = len(x_str)
            for i in range(n//2):
                if x_str[i] !=x_str[n-1-i]:
                    return False
            return True
    
# Two Sum Problem :https://leetcode.com/problems/two-sum/

    def twoSum(self, nums:list[int], target:int) -> list[int]:

        """
        Given an array of integers and a target value, find the indices of the two numbers
        that add up to the target, using each element only once.

        Args:
            nums (list[int]) : list of integers
            target (int) : the target sum

        Returns:
            list [int]: Indices of the two numbers whose sum equals the target.
        """

        n = len(nums)
        for idx1 in range(n):
            for idx2 in range(idx1+1,n):
                if nums[idx1] + nums[idx2] == target:
                    return [idx1, idx2]
                
# Roman to Integer : https://leetcode.com/problems/roman-to-integer/

    def romanToInt(self, s:str) -> int:

        """
        Converts a Roman numeral string to an integer.

        Args:
            s (str): A string representing the Roman numeral.
        
        Returns:
            int: The corresponding integer value.
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
        n = len(s)

        for i in range(n):
            current = roman[s[i]]
            if i + 1< n and roman[s[i+1]] > current:
                total -=current
            else:
                total +=current
        return total

    
    
#Longest Common Prefix :https://leetcode.com/problems/longest-common-prefix/description/

    def longestCommonPrefix(self, strs:list[str])-> str:

        """
        Returns the longest common prefix string among an array of strings.
        If there is no common prefix, returns an empty string

        Args :
            strs (list[str]): A list of strings.

        Returns:
            str: The longest common prefix shared by all strings in the list.
        """
        if not strs:
            return ""
        for i in range(len(strs[0])):
            current_char = strs[0][i]

            for word in strs[1:]:
                if i < len(word) and word[i] != current_char:
                    return strs[0][:i]
        
        return strs[0]
    
#Valid Parentheses : https://leetcode.com/problems/valid-parentheses/description/
    def isValid(self, s:str)-> bool:
        """
        Checks whether a string containing only brackets is valid.

        A valid string requires:
        - Each opening bracket to be closed by the same type of bracket.
        - Brackets to be closed in the correct order.
        - Every closing bracket to have a matching opening bracket.

        Args:
            s (str): A string containing only the characters '(', ')', '{', '}', '[' and ']'.

        Returns:
            bool : True if the string is valid, False otherwise.
        
        """
        brackets =[]
        mapping = {')':'(',
                    '}':'{',
                    ']':'['
                    }
        for char in s:
            if char in mapping.values():
                brackets.append(char)
            elif char in mapping:
                if not brackets or brackets[-1] != mapping[char]:
                    return False
                brackets.pop()
            else:
                return False
        return not brackets
    

# Merge Two Sorted Lists : https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.

    def mergeTwoLists(self, list1:list[int], list2 :list[int]) -> ListNode:
        """
        Merge two sorted singly-linked lists into one sorted linked list.

        Each list is already sorted in ascending order. The merged list should also be sorted.
        Nodes are reused from the input lists (no new nodes are created).

        Args:
            list1 (List[int]): first sorted list
            list2 (List[int]): second sorted list

        Returns:
            ListNode: Head of the merged sorted linked list

        """
        first = ListNode()
        current = first
        list1 = ListNode.from_list(list1)
        list2= ListNode.from_list(list2)

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return first.next 
        

            
            