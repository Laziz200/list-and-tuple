text="Python programming is amazing!"
words=text.split()
list=[]
new_list=[]
for word in words:
    new_list.append(word[0])
    list.append(word)
    print(word)
print("listga aylantirildi text")
print(list)
print("bosh harflari olindi")
new_text=' '.join(new_list)
print(new_text)