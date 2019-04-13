# Longest Palindromic Substring | Set 1
# Given a string, find the longest substring which is palindrome. For example, if the given string is “forgeeksskeegfor”, the output should be “geeksskeeg”.
# Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
# Method 1 ( Brute Force ) 
# The simple approach is to check each substring whether the substring is a palindrome or not. We can run three loops, the outer two loops pick all substrings one by one by fixing the corner characters, the inner loop checks whether the picked substring is palindrome or not.

# Time complexity: O ( n^3 )
# Auxiliary complexity: O ( 1 )



 

# Method 2 ( Dynamic Programming ) 
# The time complexity can be reduced by storing results of subproblems. The idea is similar to this post. We maintain a boolean table[n][n] that is filled in bottom up manner. The value of table[i][j] is true, if the substring is palindrome, otherwise false. To calculate table[i][j], we first check the value of table[i+1][j-1], if the value is true and str[i] is same as str[j], then we make table[i][j] true. Otherwise, the value of table[i][j] is made false.



# Python program 
  
import sys 
  
# A utility function to print a 
# substring str[low..high] 
def printSubStr(st,low,high) : 
    sys.stdout.write(st[low : high + 1]) 
    sys.stdout.flush() 
    return '' 
  
# This function prints the longest palindrome 
# substring of st[]. It also returns the length 
# of the longest palindrome 
def longestPalSubstr(st) : 
    n = len(st) # get length of input string 
  
    # table[i][j] will be false if substring  
    # str[i..j] is not palindrome. Else  
    # table[i][j] will be true 
    table = [[0 for x in range(n)] for y 
                          in range(n)]  
      
    # All substrings of length 1 are 
    # palindromes 
    maxLength = 1
    i = 0
    while (i < n) : 
        table[i][i] = True
        i = i + 1
      
    # check for sub-string of length 2. 
    start = 0
    i = 0
    while i < n - 1 : 
        if (st[i] == st[i + 1]) : 
            table[i][i + 1] = True
            start = i 
            maxLength = 2
        i = i + 1
      
    # Check for lengths greater than 2.  
    # k is length of substring 
    k = 3
    while k <= n : 
        # Fix the starting index 
        i = 0
        while i < (n - k + 1) : 
              
            # Get the ending index of  
            # substring from starting  
            # index i and length k 
            j = i + k - 1
      
            # checking for sub-string from 
            # ith index to jth index iff  
            # st[i+1] to st[(j-1)] is a  
            # palindrome 
            if (table[i + 1][j - 1] and 
                      st[i] == st[j]) : 
                table[i][j] = True
      
                if (k > maxLength) : 
                    start = i 
                    maxLength = k 
            i = i + 1
        k = k + 1
    print "Longest palindrome substring is: ",printSubStr(st, start, 
                                               start + maxLength - 1) 
  
    return maxLength # return length of LPS 
  
  
# Driver program to test above functions 
st = "forgeeksskeegfor"
l = longestPalSubstr(st) 
print "Length is:", l 