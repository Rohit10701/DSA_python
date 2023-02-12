from copy import deepcopy
from pandas import *
import copy
def board_valid(board,r,c):
    r_temp=r
    c_temp=c
    n=len(board)
    for i in range(n):
        if board[r][i]==1:
            return False
    for i in range(n):
        if board[i][c]==1:
            return False
    while r>=0 and c>=0:
        if board[r][c]==1:
            return False
        r-=1
        c-=1
    r=r_temp
    c=c_temp
    while r>=0 and c<=n-1:
        if board[r][c]==1:
            return False
        r-=1
        c+=1
    r=r_temp
    c=c_temp
    while r<=n-1 and c>=0:
        if board[r][c]==1:
            return False
        r+=1
        c-=1
    r=r_temp
    c=c_temp
    while r<=n-1 and c<=n-1:
        if board[r][c]==1:
            return False
        r+=1
        c+=1
    return True


def format(D_ls,res):

    for sol in D_ls:
        ls=[]
        for row in sol:
            temp=""
            for col in row:
                if col==0:
                    temp=temp+'.'
                else:
                    temp=temp+'Q'
            ls.append(temp)
        res.append(ls)
    return res



def backtrack(row,ls,board):
    n=len(board)
    if row==n:
        ls.append(board)
        return

    else:
        for i in range(n):
            if board[row][i]!=1 and board_valid(board,row,i):
                newboard=copy.deepcopy(board)
                newboard[row][i]=1
                backtrack(row+1,ls,newboard)
    return

n=4
board=[[0 for i in range(n)]for i in range(n)]
ls=[]
print(backtrack(0,ls,board))
res=[]
print(format(ls,res))