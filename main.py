from leetcode import LeetCode

if __name__ == "__main__":
    leet_obj = LeetCode()

    print ("----------- Palindrome solution ----------")

    print (" ")
    print(leet_obj.isPalindrome(121))   # True
    print(leet_obj.isPalindrome(-121))  # False
    print(leet_obj.isPalindrome(10))  # False
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
