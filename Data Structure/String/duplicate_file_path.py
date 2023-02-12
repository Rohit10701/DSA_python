def findDuplicate(paths):
        '''["root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
            "root 4.txt(efgh)"]
            
           [["root/a/2.txt",
             "root/c/d/4.txt",
             "root/4.txt"],
           
           ["root/a/1.txt",
            "root/c/3.txt"]]'''
        hm={}
        for i,ele in enumerate(paths):
            temp=[]
            ls=ele.split("(")
            
            flag=False
            for j,e in enumerate(ls):
                s=''
                k=0
                while(e[k]!=')' and len(e)==k):
                    s=s+e[k]
                    k+=1
                    if e[j]==')' or e[-1]==')':
                        flag=True
                if flag==True:
                    hm[s]=i
            
        return (hm.values())

print(findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))