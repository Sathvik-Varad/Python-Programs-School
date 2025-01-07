#creating the list
n=int(input("Enter the size of the list: "))
L=[]
for i in range (n):
    a=int(input("Enter the value/element: "))
    L.append(a)

#checking for a value
v=int(input("Enter the value to be checked: "))

if v in L:
    print(v, "is present in the list")
else:
    print(v,"is not present in the list")

#removing all negative values
for j in L:
    if j<0:
        L.remove(j)

#displaying the list
print("List= ", L)