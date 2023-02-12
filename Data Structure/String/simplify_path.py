def path(str):
    stack=[]
    cur=""

    for c in (str +"/"):
        if c=='/':
            if cur == '..':
                if stack:
                    stack.pop()
            elif cur!="" and cur !=".":
                stack.append(cur)
            cur=""
        else:
            cur+=c
    return '/'+'/'.join(stack)

print(path("/home////rohit/"))