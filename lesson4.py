a = int(input("Введите число - "))
maximum = a % 10
while a > 1 or a == 1:
    a = a // 10
    if a % 10 > maximum:
        maximum = a % 10
    if a > 9:
        continue
    else:
        print('Максимальная цифра в числе - ', maximum)
        break


