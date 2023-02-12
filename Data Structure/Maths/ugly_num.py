def isUgly(n):
        while(n!=1):
            if n%2!=0 and n%3!=0 and n%5!=0:
                return False
            if n%2==0:
                n=n//2
            elif n%3==0:
                n=n//3
            elif n%5==0:
                n=n//5
        return True

print(isUgly(6))