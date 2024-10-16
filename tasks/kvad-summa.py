# beräkning av summan av kvadraten för n
n = int(input('n?: '))
summa = 0
k = 1
while k <= n:
    summa = summa + k*k
    k += 1
print(f'Summan av kvadraterna är: {summa}')

