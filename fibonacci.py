n1=0;
n2=1;
n=int(input("Enter the number of terms you want for Fibonacci Series"));
print(n1)
for i in range(0,n):
    if(n<=1):
        next=n
    else:
        next=n1+n2
        n1=n2
        n2=next
    print(next)
    
