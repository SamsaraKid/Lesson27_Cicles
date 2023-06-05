# num = -1
# while num % 2 == 1:
#     num = int(input('введите число\n'))
#
#
# print('успех')

def f3():
    print(num + 100)
    pass

def f2():
    print(num / 2)
    pass

def f0():
    if num % 2 == 1:
        print('нечётное')
    else:
        print('чётное')
    pass



num = int(input('введите число\n'))

if len(str(abs(num))) == 3:
    f3()
elif len(str(abs(num))) == 2:
    f2()
else:
    f0()
