def anagram(s):
    # Write your code here
    if len(s)%2!=0:
        return -1
    hm1={}
    hm2={}

    for i in range(97,123):
        hm1[i]=0
    for i in range(97,123):
        hm2[i]=0
    s1=s[:int(len(s)/2)]
    s2=s[int(len(s)/2):]
    print(s1)
    print(s2)
    for ele in s1:
        if ord(ele) not in hm1:
            hm1[ord(ele)]=1
        else:
            hm1[ord(ele)]+=1
    for ele in s2:
        if ord(ele) not in hm2:
            hm2[ord(ele)]=1
        else:
            hm2[ord(ele)]+=1
    print(hm1)
    print('\n')
    print(hm2)
    diff=0
    for i in range(97,123):
        diff=diff+abs(hm1[i]-hm2[i])
    return int(diff/2)

print(anagram("aaabbb"))