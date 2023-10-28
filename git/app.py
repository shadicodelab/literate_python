name=input("Input your name: ")

if len(name)<3:
    print("Name must be at least three characters!")
elif len(name)>50:
    print("Name can be a maximum of 50 characters long!")
else:
    print("Name looks good...")



