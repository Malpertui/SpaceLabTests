from datetime import datetime, timedelta
# Define start and end dates
start_date = datetime(2020, 1, 30)
start_date_clone = datetime(2020, 1, 30) - timedelta(days=1)
all_days = 10
work_days = 2
rest_days=1
end_date = start_date + timedelta(days=all_days-4)

 
date_list_rest_days = []


print(f'Клон стартДейт {start_date_clone}')

while start_date_clone < end_date:
    start_date_clone += timedelta(days=work_days+1)
    date_list_rest_days.append(start_date_clone)
    print(start_date_clone)
    print(f'ЕндДейт внизу{end_date}')


print(f'Тільки вихідні {date_list_rest_days}')

if start_date_clone > end_date:
    print('Больше')

if start_date_clone < end_date:
    print('vtymit')


    
