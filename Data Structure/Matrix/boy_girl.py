
def count(mat):
    hm={}
    for i in range(len(mat[0])):
        hm[i]=mat[0][i]
    count=0
    for i in range(1,len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==1 and hm[j]==1:
                count+=1
            else:
                if mat[i][j]==1:
                    hm[j]+=1
    return count
mat=[[0,1,1],[1,1,1],[1,1,1]]
print(count(mat))