def longestPalindrome(s):
        maxL = 0
        ans = ""
        for i in range(len(s)):
            subStr = isPalindrome(s, i-1, i+1)
            if len(subStr) > maxL:
                maxL = len(subStr)
                ans = subStr               
            subStr = isPalindrome(s, i, i+1)
            if len(subStr) >  maxL:
                maxL = len(subStr)
                ans = subStr
        return ans
    
def isPalindrome(s, left, right):       
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            break
        left -= 1
        right += 1 
    return s[left+1:right]

print(longestPalindrome("cabzba"))