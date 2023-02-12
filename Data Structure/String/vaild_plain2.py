def checkPalin(s):
    if s==s[::-1]:
        return True
    return False


def validPalindrome(s):
        
        for i in range(len(s)):
            temp=s
            temp = list(temp)
            temp.pop(i)
            if checkPalin(temp):
                return True
        return False    

print(validPalindrome("cbbcc"))