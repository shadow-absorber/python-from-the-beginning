# import math for pi
import math

# ask user for radius
radie = input('Vad är cirkelns radie?: ')
radie = float(radie)

# if radius is smaller then 0 quit
if radie > 0:
    omkrets = 2 * math.pi * radie
    area = math.pi * radie ** 2
    print(f'Omkretsen är {omkrets:.3f}')
    print(f'Arean är {area:.3f}')
else:
    print(f'Felaktig radie!!! radie måste vara minst 1')

