# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


def fun(arr,m):
    i=0
    res=0
    while i<m:
        arr.sort()
        arr=arr[::-1]
        print(arr[0]//2)
        res=res+arr[0]//2
        arr=[-arr[0]//2+arr[0]]+arr[1:]
        i+=1
    return res
    
arr=[6,2,3,5]
m=6
print(fun(arr,m))