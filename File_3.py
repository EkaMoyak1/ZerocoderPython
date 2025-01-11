
def arithmetic(a:float, b:float, c:str):
    s = None
    if not(a and b):
        return s

    match c:
        case '+':
            s = a + b
        case '-':
            s = a - b
        case '/':
            s = a / b
        case '*':
            s = a * b
        case '^':
            s = a ** b
        case '**':
            s = a ** b
    return s

def proverka(a):
     try:
         a = float(a)
     except:
         return None
     else:
         return float(a)

print('------------ Простой калькулятор ---------------')
a = input('a = ')
b = input('b = ')
c = input('Введите операцию (+ - * / **) : ')

a, b = proverka(a), proverka(b)

result = arithmetic(a, b, c)
if result:
    print(f'{a} {c} {b} = {result}')
else:
    print('Неизвестная операция')
