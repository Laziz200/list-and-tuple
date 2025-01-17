list=[1,2,"salom",4,"ok",6.2,"salom",8,9,10]
new_list=[]
for i in list[::-3]:
    new_list.append(i)
    print(i)
new_list=tuple(new_list)
n="salom"
print(new_list)
for i in range(len(new_list)):
    if new_list[i]==n:
        print(f"{i}-chi indexda {n} bor")
