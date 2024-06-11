from datetime import datetime, timedelta

# 1.Спочатку знаходимо end_date – кінцеву дату, 
# коли закінчується кількість днів, для яких потрібно скласти розклад.
# 2.За допомогою циклу while створюємо список date_list, де поміщаємо 
# всі дати з нашого графіку (як робочі дні, так і вихідні).
# 3.За допомогою оператора del видаляємо вихідні зі списку 
# (кожен третій елемент списку).
# 4. Важливо! Це не зовсім вірне рішення. Я це розумію. Моя функція 
# складає нормальні розкладі з будь-якою кількістю усіх днів (all_days)
#  і робочих днів (work_days), але якщо поміняти значення вихідних (rest_days),
#  код працює некоректно. Розумію недолік, але не зміг вирішити. 



def make_schedule(all_days, work_days, rest_days, start_date):
    end_date = start_date + timedelta(days=all_days)
    date_list = []
    
    while start_date < end_date:    
        date_list.append(start_date)
        start_date += timedelta(days=1)
    
    del date_list[work_days::work_days+rest_days]

    return date_list

     
result = make_schedule(5, 2, 1, datetime(2020, 1, 30))
print(result)
 
