def season(month):
    if 3 <= month <= 5:
        return 'Весна'
    elif 6 <= month <= 8:
        return 'Лето'
    elif 9 <= month <= 11:
        return 'Осень'
    elif 1 <= month <= 12:
        return 'Зима'
    else:
        return 'Нет такого месяца'

m = input('Введите номер месяца: ')
if m.isnumeric():
    print(season(int(m)))


