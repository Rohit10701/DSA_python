
def multiply(num1, num2):
        n1=0
        for i in range(len(num1)):
            n1=n1+pow(10,len(num1)-i-1)*(num1[i]-ord("0"))
        n2=0
        for i in range(len(num2)):
            n2=n2+pow(10,len(num2)-i-1)*(num2[i]-ord("0"))
        print(n1,n2)

print(multiply("12","10"))