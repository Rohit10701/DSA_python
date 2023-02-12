def generate(numRows):
        ls=[]
        t=[[1],[1,1]]
        for i in range(2,numRows):
            temp=[]
            for j in range(len(t[i-1])+1):
                if j==0 or j==len(t[i-1]):
                    temp.append(1)
                else:
                    temp.append(t[i-1][j-1]+t[i-1][j])
            t.append(temp)
        return t

print(generate(5))