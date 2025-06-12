from leetcode import LeetCode

if __name__ == "__main__":
    leet_obj = LeetCode()

    print ("----------- Palindrome using slicing solution ----------")

    print (" ")
    print(leet_obj.isPalindrome_slicing(121))   # True
    print(leet_obj.isPalindrome_slicing(-121))  # False
    print(leet_obj.isPalindrome_slicing(10))  # False
    print (" ")

    print ("----------- Palindrome without slicing solution ----------")

    print (" ")
    print(leet_obj.isPalindrome_loop(121))   # True
    print(leet_obj.isPalindrome_loop(-121))  # False
    print(leet_obj.isPalindrome_loop(10))  # False
    print (" ")


    print ("----------- TwoSum solution ----------")
    print (" ")
    print(leet_obj.twoSum([3,2,4],6))   
    print(leet_obj.twoSum([2,7,11,15],9))  
    print(leet_obj.twoSum([3,3],6))
    print (" ")

    print ("----------- Roman to Integer solution ----------")
    print (" ")
    print(leet_obj.romanToInt("III"))   
    print(leet_obj.romanToInt("LVIII"))  
    print(leet_obj.romanToInt("MCMXCIV"))
    print (" ")
    

    print ("----------- Longest Common Prefix solution ----------")
    print (" ")
    print(leet_obj.longestCommonPrefix(["flower","flow","flight"]))   
    print(leet_obj.longestCommonPrefix(["dog","racecar","car"]))  
    print (" ")

    print ("----------- Valid Parentheses solution ----------")
    print (" ")
    print(leet_obj.isValid("()[]{}"))   
    print(leet_obj.isValid("(]"))
    print(leet_obj.isValid("()"))
    print(leet_obj.isValid("([])"))
    print (" ")

    print ("----------- Merge Two Sorted Lists solution ----------")
    print (" ")
    print(leet_obj.mergeTwoLists([1,2,4],[1,3,4]))  
    print(leet_obj.mergeTwoLists([],[0]))
    print(leet_obj.mergeTwoLists([],[]))
    print (" ")

    print ("----------- Remove Duplicates from Sorted Array solution ----------")
    print (" ")
    print(leet_obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  
    print(leet_obj.removeDuplicates([1,1,2]))
    print (" ")

    print ("----------- Remove Element solution ----------")
    print (" ")
    print(leet_obj.removeElement([3,2,2,3], 3))  
    print(leet_obj.removeElement([0,1,2,2,3,0,4,2],2))
    print (" ")

    print ("----------- Find the Index of the First Occurrence in a String solution ----------")
    print (" ")
    print(leet_obj.strStr("sadbutsad" ,"sad"))  
    print(leet_obj.strStr("leetcode","leeto"))
    print (" ")

    print ("----------- Search Insert Position  solution ----------")
    print (" ")
    print(leet_obj.searchInsert([1,3,5,6],5))  
    print(leet_obj.searchInsert([1,3,5,6],2))
    print(leet_obj.searchInsert([1,3,5,6],7))
    print (" ")

    print ("----------- Length of Last Word solution ----------")
    print (" ")
    print(leet_obj.lengthOfLastWord("Hello World"))  
    print(leet_obj.lengthOfLastWord("   fly me   to   the moon  "))
    print(leet_obj.lengthOfLastWord("luffy is still joyboy"))
    print (" ")

    print ("----------- Plus One solution ----------")
    print (" ")
    print(leet_obj.plusOne([1,2,3]) )
    print(leet_obj.plusOne([4,3,2,1]))
    print(leet_obj.plusOne([9]))
    print (" ")

    print ("-----------Add Binary solution ----------")
    print (" ")
    print(leet_obj.addBinary("11" ,"1") )
    print(leet_obj.addBinary("1010", "1011"))
   
    print (" ")

    print ("-----------Sqrt(x) solution ----------")
    print (" ")
    print(leet_obj.mySqrt(4) )
    print(leet_obj.mySqrt(8))
   
    print (" ")

    print ("-----------Climbing Stairs solution ----------")
    print (" ")
    print(leet_obj.climbStairs(2) )
    print(leet_obj.climbStairs(3))
   
    print (" ")

    print ("----------- Remove Duplicates from Sorted List solution ----------")
    print (" ")
    print(leet_obj.deleteDuplicates([1,1,2]) )
    print(leet_obj.deleteDuplicates([1,1,2,3,3]))
   
    print (" ")

    print ("----------- Merge Sorted Array solution ----------")
    print (" ")
    print(leet_obj.merge([1,2,3,0,0,0],3,[2,5,6],3) )
    print(leet_obj.merge([1], 1,[], 0))
   
    print (" ")