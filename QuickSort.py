"""
Quick Sort
"""
from div import divide

def qsort(item):
    def sort(left,right):
        if left == right or left> right:
            return None
        else:
            n = divide(item,left,right)
            sort(left, n-1)
            sort(n,right)
    sort(0,len(item)-1)

if __name__ == "__main__" :
    
    x = [5,1,7,9,5,3,0,2,8]
    print("=>",x)
    qsort(x)
    print(x)
    
    x = [5,1,0,3,1,4,2]
    print("=>",x)
    qsort(x)
    print(x)

    x = [5,8,6,9,7]
    print("=>",x)
    qsort(x)
    print(x)
    
    x = [5,5,5,5]
    print("=>",x)
    qsort(x)
    print(x)
    
    x = [6, 2, 8, 4, 7, 5]
    print("=>",x)
    qsort(x)
    print(x)
    
    x = [6, 2]
    print("=>",x)
    qsort(x)
    print(x)