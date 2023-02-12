w=[]

for i in range(5):
    w.append(list(map(int,input().split())))

res=[]
for i in range(5):
    for j in range(5):
        if w[i][j]==1:
            res.append(i+1)
            res.append(j+1)

print(abs(res[0]-3)+abs(res[1]-3))