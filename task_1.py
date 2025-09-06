time_str = '1h 45m,360s,25m,30m 120s,2h 60s'

time_values = time_str.split(',') #Разделяем строку по запятым

total_minutes = 0 #Объявляем переменную, куда будут записываться минуты

for time_value in time_values:
    all_values = time_value.split(' ') #Разделяем полученные из строки значения по пробелам

    minutes_in_value = 0

    #Вычисляем количество минут в каждом из временных значений
    for value in all_values:
        if 'h' in value:
            hours = int(value.replace('h', ''))
            minutes_in_value += hours * 60
        elif 'm' in value:
            minutes = int(value.replace('m', ''))
            minutes_in_value += minutes
        elif 's' in value:
            seconds = int(value.replace('s', ''))
            minutes_in_value += seconds // 60

    total_minutes += minutes_in_value

print(f"Всего минут: {total_minutes}")