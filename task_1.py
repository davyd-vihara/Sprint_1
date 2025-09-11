all_time = '1h 45m,360s,25m,30m 120s,2h 60s' #Изначальная переменная

total_time = 0

for parts in all_time.split(','):
    for i in parts.split():
        if 'h' in i:
            total_time += int(i.replace('h', '')) * 60
        elif 'm' in i:
            total_time += int(i.replace('m', ''))
        elif 's' in i:
            total_time += int(i.replace('s', '')) // 60

print('Общее количество минут = ' + str(total_time))