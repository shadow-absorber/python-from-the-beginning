Fahrenheit = float(input('Vad är temperaturen i Fahrenheit?: '))
Rankine = Fahrenheit + 459.67
Celsius = (Fahrenheit - 32) * 5 / 9
Kelvin = Celsius + 273.15

print(f'Temperaturen i Rankine är {Rankine:.2f}')
print(f'Temperaturen i Celsius är {Celsius:.2f}')
print(f'Temperaturen i Kelvin är {Kelvin:.2f}')
