world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина' #Добавил год и страну победителя

country = 'Италия'

for year in world_champions: #Вывод списка года и победителя
    print(year, '-', world_champions[year])

if country in world_champions.values(): #Проверка страны на наличие в списке победителей
    print(country + ' становилась чемпионом мира по футболу в 21 веке!')
else:
    print(country + ' не выигрывала чемпионат мира по футболу в 21 веке.')