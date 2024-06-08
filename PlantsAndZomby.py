zombies=[ 2, 1, 1, 1  ]
plants=[   1, 2, 1, 1 ]
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