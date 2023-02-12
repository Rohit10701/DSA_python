#leetcode 150
def op(op1,op2,strs):
    if strs=='+':
        return str(op1+op2)
    elif strs=='-':
        return str(op2-op1)
    elif strs=='*':
        return str(op1*op2)
    else:
        return str(op2%op1)


def evalRPN(tokens):
        stack=[]
        i=0
        while i<len(tokens):
            ele=tokens[i]
            if ele not in ['+','-','*','/']:
                stack.append(ele)
            else:
                stack.append(op(int(stack.pop(-1)),int(stack.pop(-1)),ele))
            i+=1
        return stack[-1]

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))