#leetcode 1047
def removeDuplicates(s):
        stack=[]
        for i in range(len(s)):
            if len(stack)!=0 and stack[-1]==s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        ans=""
        
        for i in range(len(stack)):
            ans=ans+stack[i]
        return ans

print(removeDuplicates("abbaca"))