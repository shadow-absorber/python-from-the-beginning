# importera math för pi
import math

# tar input för radien
radie = float(input('Vad är radien på sfären? '))

# beräknar
volymn = 4 * math.pi * radie ** 3 / 3
area = 4 * math.pi * radie ** 2

# skriver ut resultat
print(f'en sfär med radien {radie} har en volymn på {volymn} och en area på {area}')
