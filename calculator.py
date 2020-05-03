import math
while True:
    print ('1: Сложение', '2: Вычитание', '3: Умножение','4: Деление', 
    '5: Возведение в степень', '6: sin', '7: cos', '8: tan', '9: exit', sep='\n')
    f=int(input('Введите цифру действия: '))
    if f > 9:
        print('Некорректный ввод!') 
    elif f==1:
        print ('Вы вабрали сложение')
        a=float(input('Введите первое число: '))
        s=float(input('Введите второе число: '))
        d=a+s
        print (a,'+',s,'=',d)
        z = input('Нажмите Enter для продолжения')
    elif f==2:
        print ('Вы выбрали вычитание')
        a=float(input('Введите первое число: '))
        s=float(input('Введите второе число: '))
        d=a-s
        print (a,'-',s,'=',d)
        z = input('Нажмите Enter для продолжения')
    elif f==3:
        print ('Вы выбрали умножение')
        a=float(input('Введите первое число: '))
        s=float(input('Введите второе число: '))
        d=a*s
        print (a,'*',s,'=',d)
        z = input('Нажмите Enter для продолжения')
    elif f==4:
        print ('Вы выбрали деление')
        a=float(input('Введите первое число: '))
        s=float(input('Введите второе число: '))
        if s == 0:
            print('На ноль делить нельзя!')
            continue
        d=a/s
        print (a,'/',s,'=',d)
        z = input('Нажмите Enter для продолжения')
    elif f==5:
        print ('Вы выбрали возведение в степень')
        a=float(input('Введите число: '))
        s=float(input('Вкакую степень возвести: '))
        d=a**s
        print (a,'^',s,'=',d)
        z = input('Нажмите Enter для продолжения')
    elif f==6:
        print ('Вы выбрали синус числа')
        a=float(input('Введите число: '))
        d= math.sin (a)
        print ('sin',a,'=',d)
        z = input('Нажмите Enter для продолжения')
    elif f==7:
        print ('Вы выбрали косинус числа')
        a=float(input('Введите число: '))
        d= math.cos (a)
        print ('cos',a,'=',d)
        z = input('Нажмите Enter для продолжения')
    elif f==8:
        print ('Вы выбрали тангенс числа')
        a=float(input('Введите число: '))
        d= math.tan (a)
        print ('tan',a,'=',d)
        z = input('Нажмите Enter для продолжения')
    elif f == 9:
        print('Программа завершина.\n From Makers with LOVE;)')
        break
        

    