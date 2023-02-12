def foo(ls):
    count = 0
    for ele in ls:
        if ele==1:
            count+=1
    if count>=2:
        return True

n= int(input())
w=[]
for _ in range(n):
    w.append(list(map(int, input().split())))
    #w[i]=[1,1,1]
count=0
for i in range(len(w)):
    if foo(w[i])==True:
        count+=1
print(count)