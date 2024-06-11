# 1. Несортовані числа сортуються за допомогою методу sort(). Коли є 
# відсортований список, зрозуміло, що перші два числа – це найменші числа. 
# Значить треба суму їх квадратів прирівнювати до квадрату третього числа. 
# 2. Коли почав роботу над цим завданням, я не пам’ятав про sort(), 
# але пам’ятав про функції min() і max(). Намагався відсортувати так.
# 3. Додав ще внизу варіант, де дані вводить користувач. 


def check_pifagor(numbers_list):
    
    numbers_list.sort()    

    if numbers_list[0]**2 + numbers_list[1]**2 == numbers_list[2]**2:
        print(True)
    else:
        print(False)

a = [5, 3, 4] 
b = [6, 8, 10]
c = [100, 3, 65]
check_pifagor(c)



# def check_pifagor_input():
#     numbers_list = []
#     for i in range(3):
#         number = int(input('Введіть число: '))
#         numbers_list.append(number)

#     numbers_list.sort()    

#     if numbers_list[0]**2 + numbers_list[1]**2 == numbers_list[2]**2:
#         print(True)
#     else:
#         print(False)


