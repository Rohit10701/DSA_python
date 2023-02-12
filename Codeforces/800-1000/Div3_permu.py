import operator



def permu(mat):
    ls=[]
    for j in range(len(mat[0])):
        temp={}
        for i in range(len(mat)):
            ele=mat[i][j]
            if ele not in temp:
                temp[ele]=1
            else:
                temp[ele]+=1
        sorted_temp = dict( sorted(temp.items(), key=operator.itemgetter(1),reverse=True))
        for key in sorted_temp:
            if key not in ls:
                ls.append(key)
    print(*ls)





n=int(input())
ls=[]

for i in range(n):
    l=int(input())
    temp=[]
    for j in range(l):
        temp.append(list(map(int, input().split())))
    ls.append(temp)


for ele in ls:
    permu(ele)
