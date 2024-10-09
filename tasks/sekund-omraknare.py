# tar input för sekunder
sekunder_input = input('Hur många sekunder är det? ')
# omvandlar str til int
sekunder = int(sekunder_input)
# hur många timmar
timmar = sekunder // 3600
# hur många sekunder över efter timmar
sekunder = sekunder % 3600
# hur många minuter
minuter = sekunder // 60
# hur många sekunder kvar efter minuter
sekunder = sekunder % 60

# skriv ut datan lite snykt
print(f'{sekunder_input} är lika med {timmar} timmar, {minuter} minuter, och {sekunder} sekunder.')

# programmet är nu klart
print('nu är programmet klart')
print('hej då!')
