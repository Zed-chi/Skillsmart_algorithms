"""
Insertion Sorting with step
    default step is 1
"""

def swap(a,b):
    temp = a
    a = b
    b = temp
    return [a,b]
    
def sort(item, step=1):
    for i in range(0, len(item)-step):
        j=i
        print("i =",i)
        print(item)
        while j+step<len(item) and item[j]>item[j+step]:
            k=j
            item[j],item[j+step] = swap(item[j],item[j+step])
            while k-step > -1 and item[k]<item[k-step]:
                item[k],item[k-step] = swap(item[k],item[k-step])
                k = k - step
            j = j+step
        print(item)     
    return item
            

if __name__ == "__main__":
    print("\n\n")
    sort([7,6,5,4,3,2,1],4)


