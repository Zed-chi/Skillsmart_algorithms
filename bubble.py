def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i]>arr[j]:
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        
a = [2,6,9,3,47,2,1,7,9]
print(a)
bubbleSort(a)
print(a)