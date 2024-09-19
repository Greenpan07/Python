print("enter any string except for'QUIT':")
a=input().upper()
print(a)

if a=='QUIT':
    raise ValueError("the string QUIT is not allowed ")

else:
    print("successwful operation")