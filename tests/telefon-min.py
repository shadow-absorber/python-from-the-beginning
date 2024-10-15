minuter = int(input(f'Hur många minuter tror du, du kommer prata under en månad?: '))

if minuter > 66:
    print(f'Välj Plus!')
elif minuter > 33:
    print(f'Välj Normal!')
else:
    print(f'Välj kontant!')

