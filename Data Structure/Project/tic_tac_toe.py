def check_valid(board,row,col):
    if board[row][col]!=' ':
        #print('Invaild')
        return False
    
    elif board[row][col]==' ':
        return True

def victory(board):
    hm_row={}
    for row in range(len(board)):
        for col in range(len(board)):
            pos=board[row][col]
            if pos not in hm_row:
                hm_row[pos]=1
            else:
                hm_row[pos]+=1
        if hm_row[pos]==len(board):
            return True
        hm_row={}

    
    hm_col={}
    for row in range(len(board)):
        for col in range(len(board)):
            pos=board[col][row]
            if pos not in hm_col:
                hm_col[pos]=1
            else:
                hm_col[pos]+=1
        if hm_col[pos]==len(board):
            return True
        hm_col={}

    hm_dia={}
    for row in range(len(board)):
        for col in range(len(board)):
            if row==col:
                pos=board[row][col]
                if pos not in hm_dia:
                    hm_dia[pos]=1
                else:
                    hm_dia[pos]+=1
        if hm_dia[pos]==len(board):
            return True
    
    hm_opdia={}
    for row in range(len(board)):
        for col in range(len(board)):
            if row==len(board)-col-1:
                pos=board[row][col]
                if pos not in hm_opdia:
                    hm_opdia[pos]=1
                else:
                    hm_opdia[pos]+=1
        if hm_opdia[pos]==len(board):
            return True
    return False






#board=[[ ' ' for _ in range(n)] for _ in range(n)]
board=[ [0,1,0],
        [0,1,0],
        [0,1,1]]
print(victory(board))