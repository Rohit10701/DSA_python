global t
def pow1(x,n):
    global t
    t=[1]
    if(n==0):
        return t[n]
    elif(n>0):
        if n-1<len(t):
            t.append(x*t[n-1])
        else:
            t.append(x*pow1(x,n-1))
    else:
        if n+1<len(t):
            t.append((1/x)*t[n+1])
        else:
            t.append((1/x)*pow1(x,n+1))
    return t[n]
  
print(pow1(2,5))