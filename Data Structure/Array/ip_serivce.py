
def partition(ls):
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

def convert(R,ls):
    for ele in R:
        t1=ele[1][:2]+ele[1][3:5]+ele[1][6:]
        t2=ele[2][:2]+ele[2][3:5]+ele[2][6:]
        temp=[t1,t2]
        ls.append(temp)
    return ls
    

def solve(N,R):
    ls=[]
    return partition(convert(R,ls))

N=int(input())
R=[input().split() for i in range(N)]

out_=solve(N,R)
print(out_)