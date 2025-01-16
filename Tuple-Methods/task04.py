my_tuple = (1,2,3,2,4,2,5)
max_count = 0
for element in my_tuple:
    count = my_tuple.count(element)
    if count > max_count:
        max_count = count
        

print(f"Eng kop takrorlanish soni: {max_count}")
