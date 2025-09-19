types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

tickets_by_type = {} # Создаем итоговый словарь

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

def tickets_by_type(types, tickets):
    used = []
    result = {}
    for key in types:   # идём просто по словарю types
        current = []
        for ticket in tickets.get(key, []):
            if ticket not in used:
                current.append(ticket)
                used.append(ticket)
        result[types[key]] = remove_duplicates(current)
    return result

tickets_by_type = tickets_by_type(types, tickets)
print(tickets_by_type)