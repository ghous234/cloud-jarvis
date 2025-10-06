def binary_search(arr,x):
      l=0
      r=len(arr)-1
while l<=r:
        mid = l+(r-1)//2
        if arr[mid]==x:
           return mid
        elif arr[mid]< x:
          l= mid+1
        else:
          r=mid-1
       return -1
arr=[41,54,63,45,23]
x=45
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

