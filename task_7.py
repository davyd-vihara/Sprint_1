def digit_root(num):
    if num < 1 or num > 10**7: # Проверка числа на соответствие
        return 'Ошибка: число должно быть от 1 до 10^7'
    elif num < 10: # Здесь просто возвращаем число
        return num
    else:
        digits = []
        for char in str(num):
            digits.append(int(char))
            sum_digits = sum(digits)
        return digit_root(sum_digits)

print(digit_root(10)) # 1
print(digit_root(9824)) # 5
print(digit_root(515718)) # 9
print(digit_root(21665156)) # Ошибка
print(digit_root(-1)) # Ошибка
print(digit_root(0)) # Ошибка