# importera random bibloteket för att räkna med tärningar
import random

# kasta två tärningar och räkna resultatet
tärning_ett = random.randint(1,6)
tärning_två = random.randint(1,6)
resultat = tärning_ett + tärning_två

# skriv ut resultatet
print(f'Tärningarna är kastade')
print(f'Du fick {tärning_ett} och {tärning_två} vilket tilsamans blir {resultat}')
