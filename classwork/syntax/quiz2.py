l = list()
for i in range(1,6):
    temp = int(input("number " +str(i) +": "))
    l.append(temp)
sum = 0
max = l[0]
i=1

for n in l:
    sum+=n

while i<len(l):
    if l[i]>max:
        max = l[i]
    i+=1

print("sum:",sum)
print("max:",max)