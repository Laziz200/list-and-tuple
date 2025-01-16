list=[13,-1,-5,99,-7,32,"Salom"]
new_list=[]
for i in list[0:]:
    if isinstance(i,(int,float)):
        if i>=0:
            new_list.append(i)
    if isinstance(i,str):
        new_list.append(i.lower())
print(new_list)