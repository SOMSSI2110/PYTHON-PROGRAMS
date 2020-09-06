n=int(input("Enter number of elements for the list"))
list=[]
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
print("Positive Numbers:")
for i in range(0,n):
    if(list[i]>0):
        print(list[i]);

    
