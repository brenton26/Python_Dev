'''
This program determines if a sentence is a palindrome or not.
'''
def isPalindrome(s):
  
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c     
        return ans
  
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
         return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

s = input("Give sentence: ")
if isPalindrome(s):
    print("That WAS a palindrome.")
else:
    print("That was NOT a palindrome.")
    