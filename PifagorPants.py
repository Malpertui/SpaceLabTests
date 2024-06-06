numbers_list = list(input("Введіть 3 числа: " ))
numbers_list_int = []
for i in range(len(numbers_list)):
    int_number = int(numbers_list[i])
    numbers_list_int.append(int_number)

min_number = min(numbers_list_int)
print(min_number)
max_number = max(numbers_list_int)
print(max_number)
numbers_list_int.remove(max_number)
numbers_list_int.remove(min_number)
medium_number = numbers_list_int[0]
print(medium_number)
numbers_list_final = []
numbers_list_final.append(min_number)
numbers_list_final.append(medium_number)
numbers_list_final.append(max_number)



    

if numbers_list_int[0]**2 + numbers_list_int[1]**2 == numbers_list_int[2]**2:
    print("True")
else:
    print('False')
