def generateMatrix(n):
        left=0
        right=n-1
        top=0
        down=n-1
        val=1
        mat=[[0 for i in range(n)] for k in range(n) ]
        
        while(left<=right and top<=down):
            for i in range(left,right+1):
                mat[top][i]=val
                val+=1
            top+=1
            for i in range(top,down+1):
                mat[i][right]=val
                val+=1
            right-=1
            for i in range(right,left-1,-1):
                mat[down][i]=val
                val+=1
            down-=1
            for i in range(down,top-1,-1):
                mat[i][left]=val
                val+=1
            left+=1
        return mat


print(generateMatrix(3))