


a=[[0,30],[5,10],[15,20],[5,15]]

def countRoom(ls):
    start=[]
    end=[]
    for i in range(len(ls)):
        start.append(ls[i][0])
    start.sort()
    for i in range(len(ls)):
        end.append(ls[i][1])
    end.sort()

    s=0
    e=0
    count=0
    max_count=0
    while s<len(end):
        if start[s]<end[e]: 
            count+=1
            s+=1
        else:
            count-=1
            e+=1
        max_count=max(count,max_count)
    return max_count

print(countRoom(a))