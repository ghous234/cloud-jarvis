lst=[30,50,60,5,100]
n=len(lst)
for i in range(n):
    for j in range(0,n-i-1):
        if lst[j] > lst[j+1]:
         lst [j], lst[j+1]= lst [j+1], lst [j]
         print("sorted list is:", lst) 


