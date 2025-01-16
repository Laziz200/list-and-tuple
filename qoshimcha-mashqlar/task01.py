list=[1,2,45.7,"salom","ok",True,"task"]
new_list=[]
for i in list:
    if isinstance(i,str):
        new_list.append(i.upper())
print(new_list)