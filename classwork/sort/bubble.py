def bubbleSort(l: list):
    for _ in range(len(l)-1):
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                temp = l[i]
                l[i]=l[i+1]
                l[i+1]=temp
    return l

print(bubbleSort([5,9,6,1,8,7,3,4,2,0]))