text="Learning Python is fun!"
list=[]
for i in text.split():
    list.append(i)
    print(i)
print("har bir elementni royxatga ajratilib listga qoshildi!")
print(list)
print("list tuplega ozgartirildi!")
tuple=tuple(list)
print(tuple)
for i in tuple:
    if i==tuple[-1]:
        n=tuple.index(i)
        print(f"oxirgi sozning indexi = {n}")