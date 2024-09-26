y = int(input("y = "))
if y>10:
    if y%2==0:
        print("y is greater than 10 and even")
    else:
        print("y is greater than 10 and odd")
else:
    if y>0:
        print("y is 10 or less and positive")
    else:
        print("y is 10 or less and zero or negative")