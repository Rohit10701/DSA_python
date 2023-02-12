def spiralOrder(mat):
        left=0
        right=len(mat[0])-1
        top=0
        down=len(mat)-1
        
        ls=[]
        
        while(left<=right and top<=down):
            for i in range(left,right+1):
                ls.append(mat[top][i])
            top+=1
            for i in range(top,down+1):
                ls.append(mat[i][right])
            right-=1
            if (left<=right):
                for i in range(right,left-1,-1):
                    ls.append(mat[down][i])
                down-=1
            for i in range(down,top-1,-1):
                ls.append(mat[i][left])
            left+=1
        return ls
        
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))