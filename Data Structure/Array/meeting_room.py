a=[[0,3],[17,20],[2,10]]

def check(Mat):
    Mat.sort()
    #print(Mat)
    for i in range(1,len(Mat)):
        if Mat[i-1][1]>Mat[i][0]:
            return False
    return True


print(check(a))