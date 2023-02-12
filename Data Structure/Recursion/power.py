def foo(n,p,res):
    if p==0:
        return res
    else:
        return n*foo(n,p-1,res)
    
res = 1
print(foo(10,3,res))