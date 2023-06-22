N = abs(int(input()))
A_e = input("Введите элементы списка через пробел: ").split()
A_n = list(map(int, A_e))
if len(A_n) != N:
    print('Некорректное число')
else:
    X = int(input('Введите число, которое необходимо найти в списке: '))
    count = 0
    for i in range(N):
        if A_n[i] == X:
            count += 1
    print(f'Число {X} встречается в списке A {count} раз')