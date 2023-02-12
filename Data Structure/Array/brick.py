def subSum(ls):
    sum=0
    res=[]
    for ele in ls:
        sum=sum+ele
        res.append(sum)
    return res

def leastBricks( wall) -> int:
        ls=[]
        hm={}
        for brick in wall:
            ls = ls + subSum(brick)
            
        for ele in ls:
            if ele not in hm:
                hm[ele]=1
            else:
                hm[ele]+=1
        hm = dict(sorted(hm.items(), key=lambda item: item[1]))
        key = list(hm.keys())
        val = list(hm.values())
        print(key)
        if len(key)>1:
            return len(wall)- key[-2]
        return len(wall)- key[-1]

print(leastBricks([[1],[1],[1]]))