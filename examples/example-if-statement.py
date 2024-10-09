x = int(input('Skriv ett heltal! '))
if x < 24:
	print("denna raden körs om if-satsen är sann")
	print("")
	print(f'x är {x}, vilket är mindre än 24')
else:
    print("if satsen är falsk")
    print(f'x är {x}, vilket är större än 24')
print("denna raden är inte en del av if-satsen")
