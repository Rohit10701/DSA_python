w=list(map(int,input().split()))
s=list(map(int,input().split()))

n=w[0] 
k=w[1]

count=0
for ele in s:
    if ele>=s[k-1] and ele>0:
        count+=1

print(count)