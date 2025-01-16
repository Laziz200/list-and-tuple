list=[13,-1,-5,99,-7,32]
new_list=[]
for i in list[0:]:
    if isinstance(i,(int,float)):
        if i>=0:
            new_list.append(i)
print(new_list)