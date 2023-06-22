N = abs(int(input()))
A_e = input("Введите элементы списка через пробел: ").split()
A_n = list(map(int, A_e))
if len(A_n) != N or N == 0:
    print('Некорректное число')
else:
    X = int(input('Введите число, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - A_n[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_n[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A_n[index]} в Вашем списке близко к числу {X}')