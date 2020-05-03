while True:
    finish = input('Нажмите enter или введите exit для завершения: ')
    if finish == 'exit':
        print('Программа завершина.\nFrom Makers with LOVE;)')
        break
    try:
        x = float(input('Введите 1ое число: '))
    except ValueError:
        print('Некорректный ввод!\n1ое число!')
        continue
    z = input('+, -, /, *, **: ')
    try:
        y = float(input('Веедите 2ое число: '))
    except ValueError:
        print('Некорректный ввод!\n1ое число!')
        continue
    if y == 0:
            print('На ноль делить нельзя!')
            continue
    elif z == '+':
        print(f'{x} + {y} = {x+y}')
    elif z == '-':
        print(f'{x} - {y} = {x-y}')
    elif z == '/':
        print(f'{x} / {y} = {x/y}')
    elif z == '*':
        print(f'{x} * {y} = {x*y}')
    elif z == '**':
        print(f'{x}^{y} = {x**y}')
    elif z != '+' or '-' or '/' or '*' or '**':
        print('Некорректный ввод!')
    


    