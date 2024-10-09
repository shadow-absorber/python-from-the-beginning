# läser in två data punkter
pris_med_moms = float(input('Vad kostar varan med moms? '))
moms_sats = float(input('Vad är moms satsen? '))

# beräknar
utan_moms = pris_med_moms / (1+moms_sats/100)
moms = utan_moms * moms_sats/100

# skriver ut datan
print(f'Varan kostar {pris_med_moms:.3f} med moms och moms satsen är {moms_sats:.3f}')
print(f'Utan moms kostar varan {utan_moms:.3f}.')
print(f'Momsen är {moms:.3f} på den här varan.')

# slut
print('nu är programmet slut. hej då!')
