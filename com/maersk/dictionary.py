d = {}
# print(type(d))
n = int(input("Enter number of students: "))
i=1
while i<=n:
    name = input("Enter Student name: ")
    age = int(input("Enter the age: "))
    d[name]=age
    i = i+1
print("------------------------------")
print("\t Name \t \t Age")
for x in d:
    print("\t", x, "\t\t", d[x])

v = input("Please enter the value to delete: ")

v1 = d.get(v, "notfound")

if v1 == "notfound":
    print(v, " Key does not exist")
else:
    del d[v]

print("------------------------------")
print("-----------New List-----------")
print("\t Name \t \t Age")
for x in d:
    print("\t", x, "\t\t", d[x])
