def bubbleSort(l: list):
    for _ in range(len(l)-1):
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                switch(l,i,i+1)
    return l

def selectionSort(l: list):
    for i in range(len(l)):
        min = i
        for j in range(i,len(l)):
            if l[j]<l[min]: min=j
        switch(l,i,min)
    return l

def insertionSort(l: list):
    for i in range(len(l)):
        cur = l[i]
        for j in reversed(range(0,i)):
            if cur<l[j]:
                switch(l,j,j+1)
    return l
    
def switch(l,a,b):
    temp = l[a]
    l[a]=l[b]
    l[b]=temp
    return l

def mergeSort(l, left, right):
    if right-left<=1:
        return 
    mid = (right+left)//2
    mergeSort(l,left,mid)
    mergeSort(l,mid,right)
    merge(l,left,mid,right)

def merge(l,left,mid,right):
    result = []
    le=left
    ri=mid
    while le<mid and ri<right:
        if l[le]<l[ri]:
            result.append(l[le])
            le+=1
        elif l[ri]<l[le]:
            result.append(l[ri])
            ri+=1
    result.extend(l[le:mid])
    result.extend(l[ri:right])
    for i in reversed(range(left,right)):
        l[i]=result.pop()

def quickSwitch(l,left,right):
    pivot = l[right]
    c=left-1
    for i in range(left,right):
        if l[i]<pivot:
            c+=1
            temp = l[c]
            l[c]=l[i]
            l[i]=temp
    temp = l[c+1]
    l[c+1]=l[right]
    l[right]=temp
    return c+1

def quickSort(l, left, right):
    if left<right:
        pivot = quickSwitch(l,left,right)
        quickSort(l,left,pivot-1)
        quickSort(l,pivot+1,right)

print(bubbleSort([5,9,6,1,8,7,3,4,2,0]))
print(selectionSort([5,9,6,1,8,7,3,4,2,0]))
print(insertionSort([5,9,6,1,8,7,3,4,2,0]))
arr = [5,9,6,1,8,7,3,4,2,0]
mergeSort(arr,0,10)
print(arr)
arr = [5,9,6,1,8,7,3,4,2,0]
quickSort(arr,0,9)
print(arr)