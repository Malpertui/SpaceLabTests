
numbers_list = []
for i in range(3):
    number = int(input('Введіть число: '))
    numbers_list.append(number)

numbers_list.sort()    

if numbers_list[0]**2 + numbers_list[1]**2 == numbers_list[2]**2:
    print(True)
else:
    print(False)
