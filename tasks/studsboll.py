höjd = float(input('Hur högt up släptes bollen?: '))
gånger = 0
while höjd > 0.01:
    höjd = höjd * 0.7
    gånger += 1
print(f'Bollen studsar {gånger} antal gånger!')
