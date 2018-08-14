"""
dividing
"""

def divide(arr,a1=None,a2=None):
    i1 = 0 if a1==None else a1
    i2 = (len(arr) - 1) if a2==None else a2
    n = arr[i1]
    while i1<i2:
        while arr[i1]<n:
            if i1+1 < i2:
                i1+=1
            else:
                break
        while arr[i2]>n:
            if i2-1 > i1:
                i2-=1
            else:
                break
        if arr[i1]==arr[i2] and i1<i2-1:
            i1+=1
            i2-=1
        if arr[i1]>arr[i2]:
            t = arr[i1]
            arr[i1] = arr[i2]
            arr[i2] = t
        if i1==i2 or i1 == i2-1:
            break
    return i2

if __name__ == "__main__" :
    x = [5,1,7,9,5,3,0,2,8]
    print("=>",x)
    divide(x)
    print(x)
    
    x = [5,1,0,3,1,4,2]
    print("=>",x)
    divide(x)
    print(x)
    
    x = [5,8,6,9,7]
    print("=>",x)
    divide(x)
    print(x)
    
    x = [5,5,5,5]
    print("=>",x)
    divide(x)
    print(x)
    
    x = [6, 2, 8, 4, 7, 5]
    print("=>",x)
    divide(x)
    print(x)
    
    x = [6, 2]
    print("=>",x)
    divide(x)
    print(x)