def bsearch(arr, item):
    reversed = True if arr[0]>arr[len(arr)-1] else False
    if len(arr) == 2:
        if item == arr[0]:
            return 0
        elif item == arr[1]:
            return 1
        else:
            return None
    mid = len(arr)//2
    if arr[mid] == item:
        return mid
    elif item > arr[mid]:
        if reversed == False:
            res = bsearch(arr[mid:],item)
            return (res+mid) if res!=None else None
        return bsearch(arr[:mid+1], item)
    else:
        if reversed == True:
            res = bsearch(arr[mid:],item)
            return (res+mid) if res!=None else None
        return bsearch(arr[:mid+1], item)
    
print(bsearch([199,85,65,45,23,12,10,8,5,1],1))