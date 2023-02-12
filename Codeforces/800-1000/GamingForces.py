def foo(ls):
    ls.sort()
    count=0
    #1 1 2
    ones = 0
    for i in range(len(ls)):
        if ls[i]==1:
            ones+=1
    rem = len(ls)-ones
    if ones%2 ==0:
        count = int(ones//2)+rem
    else:
        count = int(ones//2)+1+rem
    print(count)

n=int(input())
w=[]
for _ in range(n):
    x= int(input())
    w.append(list(map(int,input().split())))

for ele in w:
    foo(ele)