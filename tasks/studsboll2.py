# räknar hur många gånger en studsboll studsar
while True:
    höjd = float(input('Hur högt up släpper du bollen? skriv ett negativt tal för att avbryta!: '))
    if höjd < 0:
        break
    gånger = 0
    while höjd > 0.01:
        höjd = höjd * 0.7
        gånger += 1
    print(f'Studsbollen studar {gånger:.3f} gånger!')

