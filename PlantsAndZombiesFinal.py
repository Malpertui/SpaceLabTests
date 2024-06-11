# 1. Cпочатку ми вводимо дві змінні: zombies_score і plants_score і надаємо 
# їм значення нуль. 
# Потім ми порівнюємо довжину списку з числами (тобто порівнюємо кількість 
# бійців).
# Якщо списки однакової довжини, ми по порядку порівнюємо кожні два числа з обох
#  списків. Де число більше, той список (та команда) отримує +1 до свого score. 
# Якщо числа однакові, обидві команди втрачають очко. 
# 2. Потім порівнюємо zombies_score і plants_score. Якщо кількість очок 
# однакова, додаємо числа зі списків і порівнюємо суму чисел. 
# 3. Далі розглядаємо варіант, якщо кількість бійців (чисел у списках) різна. 




def plants_fight_zombies(zombies, plants):
    zombies_score=0
    plants_score=0 
    if len(zombies) == len(plants):
        for i in range(len(zombies)):
            if zombies[i] > plants[i]:
                zombies_score+=1
            elif plants[i] > zombies[i]:
                plants_score+=1
            else:
                zombies_score-=1
                plants_score-=1  


        if  plants_score>zombies_score:
            print(True)
        elif plants_score==zombies_score:
            sum_zombies = 0
            for num in zombies:
                sum_zombies+=num
            
            sum_plants = 0
            for num in plants:
                sum_plants+=num

            if sum_zombies>sum_plants:
                print(False)
            else:
                print(True) 
        else:
            print(False)

    elif len(zombies) > len(plants):
        for i in range(len(plants)):
            if zombies[i] > plants[i]:
                zombies_score+=1
            elif plants[i] > zombies[i]:
                plants_score+=1
            else:
                zombies_score-=1
                plants_score-=1

        if len(zombies) - plants_score > len(plants) - zombies_score:
            print(False)

        elif len(zombies) - plants_score == len(plants) - zombies_score:
            sum_zombies = 0
            for num in zombies:
                sum_zombies+=num
            
            sum_plants = 0
            for num in plants:
                sum_plants+=num

            if sum_zombies>sum_plants:
                print(False)
            else:
                print(True)
        else:
            print(True) 


zombies=[ 2, 1, 1, 1  ]
plants=[   1, 2, 1, 1 ]

zombies2=[ 1, 3, 5, 7 ] 
plants2=[ 2, 4 ]

zombies3=[ 1, 3, 5, 7 ] 
plants3=[ 2, 4, 0, 8 ]

zombies4=[ 1, 3, 5, 7 ] 
plants4=[ 2, 4, 6, 8 ]

plants_fight_zombies(zombies2, plants2)
