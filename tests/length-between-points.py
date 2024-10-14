# import math lib for sqrt
import math

# get input from user
x1 = float(input('Vad är x1?: '))
x2 = float(input('Vad är x2?: '))
y1 = float(input('Vad är y1?: '))
y2 = float(input('Vad är y2?: '))


distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f'avståndet mellan punkterna är {distance:.3f}')
