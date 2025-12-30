def Selection_sort(arr):
    n=len(arr)
    for i in range(n):
        lower =i
        for j in range(i+1,n):
            if arr[j]<arr[lower]:
                lower=j
        arr[i],arr[lower]=arr[lower],arr[i]
        
       
        
        
arr=[8,2,6,3,1,4,7,9,8]
Selection_sort(arr)
print("Sorted array:",arr)
