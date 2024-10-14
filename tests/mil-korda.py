mil_nu = int(input('Antal mil i dag?: '))
mil_föra_år = int(input('Antal mil föra året?: '))
print(f'Mil körda {mil_nu - mil_föra_år}')

liter_bränsle = float(input('Antal liter bränsle?: '))
liter_per_mil = liter_bränsle/(mil_nu - mil_föra_år)
print(f'Förbrukning pär mil: {liter_per_mil:.3f}')

