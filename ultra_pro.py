# Начало игры answ = 'y'
answ = 'y'
while(answ == 'y' or answ=='Y'):
# Ввод искомого числа
    num = input("Введите число от 1 до 100 ")
    if not num.isdigit():
        print("It is not number")
        continue
    num = int(num)
    if(num < 1 or num > 100):
        print('the number must be in the range from 1 to 100')
        continue
#  Конец ввода
    lb = 1
    rb = 100
    mashine_num = (lb + rb) // 2
#  Цикл по определению числа
    while(num != mashine_num):
        mashine_num = (lb + rb) // 2
        s1 = 'Число больше ' + str(mashine_num) + ' ? (y/n) '
        sk = input(s1)
        if(sk == 'y' or sk == 'Y'):
# rb = rb
            lb = mashine_num
        elif(sk == 'n' or sk == 'N'):
# lb = lb
            rb = mashine_num
        else:
            print('Введите правильный ответ "y" или "n"')
            continue
        if(rb-lb) <= 3:
            s1 = ' Это число = ' + str(lb)+'?  y/n '
            sk = input(s1)
            if (sk == 'y' or sk == 'Y'):
                mashine_num=lb
                print('Это число =',mashine_num)
                break
            elif(sk == 'n' or sk == 'N'):
                s1 = ' Это число = ' + str(lb+1) + '?  y/n '
                sk = input(s1)
                if (sk == 'y' or sk == 'Y'):
                    sk = input(s1)
                if (sk == 'n' or sk == 'N'):
                    mashine_num = rb if(sk == 'y' or sk == 'Y') else lb+2
                    print("Это число ",mashine_num)
        else:
            continue
    answ = input('Сыграем еще раз ? y/n ')





