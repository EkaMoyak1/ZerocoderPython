def s_sq(a:int):
    p = 4 * a
    s = a ** 2
    d = 2 * s ** 0.5
    return (p, s, d)

a = input('Введите сторону квадрат:')
# нужно сначала проверить: введено число или нет. А число может содержать "."
if a.replace('.','',1).isnumeric():
    print(s_sq(float(a)))



