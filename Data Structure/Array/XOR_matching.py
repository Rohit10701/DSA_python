# 1 2 3
# 5 6 7
a=[0,1]
b=[0,2]
count=0
res=[]
for i in range(len(a)):
    for j in range(len(b)):
        res.append(a[i]^b[j])
hm={}
for ele in res:
    if ele not in hm:
        hm[ele]=1
    else:
        hm[ele]+=1
ans=[]
for key in hm:
    if hm[key]==len(a):
        ans.append(key)
        count+=1
ans.sort()
print(count)
print(ans)


