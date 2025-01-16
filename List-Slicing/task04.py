list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
new_list=[]
for i in list[:]:
    if i==list[0] or i==list[-3] or i==list[-2] or i==list[-1]:
        new_list.append(i)
    print(i)
print(new_list)