from datetime import datetime, timedelta
# Define start and end dates
start_date = datetime(2020, 1, 30)
start_date_clone = start_date
all_days = 5
work_days = 2
rest_days=1
end_date = start_date + timedelta(days=all_days)
print(f'ЕндДейт внизу {end_date}')
 
# Initialize an empty list
date_list = []
# date_list.append(start_date)
date_list_rest_days = []

 
# Loop through the range of dates and append to the list
# print(f'Вихідні {start_date + timedelta(days=1*work_days)}')
# i =0


while start_date < end_date:
    
    date_list.append(start_date)
    start_date += timedelta(days=1)

# print(date_list)
# i =0
# date_list_rest_days = []
# while i < all_days:
#     if 

del date_list[work_days::work_days+rest_days]

print(date_list)

    


#     print(i)
#     print(start_date)
#     # print(date_list)
#     # i+=1

# print(date_list)
# print(f'Клон стартДейт {start_date_clone}')
# # i=0
# while start_date_clone < end_date:
#     start_date_clone += timedelta(days=work_days+1)
#     date_list_rest_days.append(start_date_clone)
#     print(start_date_clone)
#     print(f'ЕндДейт внизу{end_date}')
#     # i+=1
#     if start_date_clone == end_date:
#         break


# print(f'Тільки вихідні {date_list_rest_days}')

# if start_date_clone > end_date:
#     print('Больше')

    






 
# Print the list of dates
# print(date_list)