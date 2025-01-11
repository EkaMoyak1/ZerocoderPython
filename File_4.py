def is_year_leap(year:int):
    if year % 4 == 0:
        return True
    else:
        return False

year = input('Введите год:')
if year.isnumeric():
    print(is_year_leap(int(year)))



