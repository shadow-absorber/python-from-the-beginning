# importera math bibloteket för pi
import math

# läser in cirklens radie
radie = float(input('Vad är cirkelns radie? '))

# räknar ut omkrets och area
omkrets = 2 * math.pi * radie
area = math.pi * radie ** 2

# skriver ut resultatet
print(f'En cirkel med radien {radie:.3f} har omkretsen {omkrets:.3f} och arean {area:.3f}')

# nu är programet slut
print('nu är det färdig räknat')
print('hej då')
