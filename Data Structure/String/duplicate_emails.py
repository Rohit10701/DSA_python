def simplify(str):
    stack=[]
    res=""
    i=0
    for ch in str:
        if ch=='+' or i==len(str):
            break
        elif ch=='.':
            continue
        else:
            res=res+ch
        i+=1
    return res                

def numUniqueEmails(emails):
        ls=[]
        for ele in emails:
            new_email=simplify(ele.split('@')[0])+ele.split('@')[1]
            if new_email not in ls:
                ls.append(new_email)
                
        return len(ls)

print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))