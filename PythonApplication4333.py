#1 задание

#f=int(input("Введите число от 1 до 9  "))
#if f>9:
#    print("Меньше 9 нельзя")
#else:
#    a=str("  ^---^")
#    b=str(" ( o o )")
#    c=str("  ! = !/)")
#    print(a*f)
#    print(b*f)
#    print(c*f)

#2 задание

#p = int(input("Показатель степени: "))
#r = int(input("Предел: ")) 
#s = 1
#while s ** p <= r:
#    print(s ** p, end=' ')
#    s += 1
 
#print("\rПоследнее число,")
#print(" возведенное в степень:", s - 1)

#4 задание

#k = 1
#for i in range(0,25,3):
#    k *=3
#print(k)

#3 задание

#from random import *
#max=0
#min=5
#ljudi=randint(1,25)
#for i in range(ljudi):
#    grade=randint(1,5)
#    if grade<5:
#        grade=grade+random()
#        grade=round(grade)
#    print(grade, end=" ")
#    if grade>max:
#        max=grade
#    if grade<min:
#        min=grade

#5 задание

#a=int(input("Сколько котлет у губки боба - "))
#b=(input("сколько на одну сковородку помещается котлет"))
#for i in range (a):
#    c=a//b
#print(f"Понадобится {c} сковородки")




















































































































print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Введите целое число => "))))
        break
    except ValueError:
         print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c==b==a
    paaris == 0
    paaritu == 0
    while b > 0:
            if b%2==0:
                paaris+=1
            else:
                    paaritu+=1
            b = b // 10
    
    print("Чётных цифр:",paaris)
    print("Нечётных цифр:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
         b += number
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз")
    print()
    if c % 2==0:
        print("с - чётное число. Делим на 2.")
    else:
        print("с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c!=1:
            if c % 2 == 0:
                    c==c//2
            else:
                    c==(3*c + 1)//2:
print("",c)
print()
print("Гипотеза верна")




