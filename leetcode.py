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
        

# Remove Duplicates from Sorted Array : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

    def removeDuplicates(self, nums:list[int]) -> list[int]:
        
        """
        Removes duplicates in-place from a sorted list of integers so 
        that each unique element    appears only once.
        The relative order of the elements is preserved. Returns the number of unique elements(k).

        Args:
            nums (List[int]): A list of integers sorted in non-decreasing order.

        Returns:
            int: The number of unique elements (k), 
            where the first k elements in nums are the unique values.
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i + 1]
            else:
                i += 1
        return nums
    
#Remove Element : https://leetcode.com/problems/remove-element/description/

    def removeElement(self, nums:list[int], val:int)-> list[int]:
        """
            Removes all occurrences of the given value `val` from the list `nums` in-place, 
            and returns the number of elements that are not equal to `val`.

            Args:
                nums (List[int]): List of integers to process.
                val (int): The integer value to remove from the list.

            Returns:
                int: The number of elements remaining in the list after removal of `val`.
                    The list `nums` is modified in-place, 
                    with the first `k` elements containing the valid values.

        """
        
        return [x for x in nums if x!= val]

#  Find the Index of the First Occurrence in a String : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

    def strStr(self,haystack:str, needle:str)->int:
            """
            Finds the index of the first occurrence of 'needle' in 'haystack'. 
            Returns -1 if 'needle' is not found.

            Args:
                haystack (str): The string to search within.
                needle (str): The substring to find.

            Returns:
                int: The index of the first occurrence of 'needle' in 'haystack', or -1 if not found.
            """
            if needle =="":
                return 0
            needle_lenght = len(needle)
            haystack_lenght = len(haystack)
            for i in range(haystack_lenght - needle_lenght + 1):
                
                if haystack[i:i+needle_lenght] == needle:
                    return i
            return -1
    
# Search Insert Position : https://leetcode.com/problems/search-insert-position/description/
            
    def searchInsert(self, nums:list[int], target:int) -> int:
        """
        Given a sorted array of distinct integers and a target value,
        return the index if the target is found; otherwise, return the index
        where it should be inserted to maintain the sorted order.

        Args:
            nums (List[int]): A sorted list of distinct integers.
            target (int): The value to search for in the list.

        Returns:
            int: The index of the target if found, or the index where it should
                 be inserted to keep the list sorted.
        """
        left , right = 0 , len(nums)-1
        while left<= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid -1
        return left
    
#  Length of Last Word : https://leetcode.com/problems/length-of-last-word/description/

    def lengthOfLastWord(self, s:str) -> int:
        """
            Given a string `s` that consists of words and spaces, 
            this function returns the length of the last word in the string.
            A word is defined as the longest sequence of non-space characters.

        Args:
            s (str): A string containing words separated by spaces.

        Returns:
            int: The length of the last word in the string.
        """

        words = s.split()
        for i, word in enumerate (words):
            if i == len(words)-1:
                return len(word)
            
# Plus One :  https://leetcode.com/problems/plus-one/description/        
    def plusOne(self, digits:list[int])->list[int]:
            """
            Function to increment a large integer represented as an array of digits.

            Args:
                digits (List[int]): An array representing a large integer, 
                where each element is a digit (0–9).

                Return:
                    List[int]: A new array representing the original integer incremented by 1.

            """

            n = len(digits)
            for i in range(n-1,-1,-1):
                if digits[i]<9 :
                    digits[i] +=1
                    return digits
                digits[i] = 0
            return [1]+[0]*n
    
#Add Binary :https://leetcode.com/problems/add-binary/description/
    def addBinary(self, a:str, b:str) ->str:
        """
        Adds two binary strings and returns their sum as a binary string.

        Args:
            a (str): A binary string 
            b (str): A binary string 

        Returns:
            str: The binary sum of the two input strings.
        """
        
        result = ""
        carry = 0

        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry
            carry = total // 2
            result = str(total % 2) + result

            i -= 1
            j -= 1

        return result

#Sqrt(x) :https://leetcode.com/problems/sqrtx/description/
          
    def mySqrt(self, x:int)->int:
        """
        Function to compute the integer square root of a non-negative integer x, 
        rounded down to the nearest whole number.

        Args:
            x (int): A non-negative integer whose square root is to be computed.

        Returns:
            int: The square root of x, rounded down to the nearest integer. 
            The result is also non-negative.

        """
        if x<2 :
            return x
        left , right =0,x
        while left <= right:
            mid = (left + right)//2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid -1
        return right

       