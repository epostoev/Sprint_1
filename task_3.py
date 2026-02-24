world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = "Аргентина"

for year_winner, country_winner in world_champions.items():
    print(f"{year_winner} - {country_winner}")

country = 'Италия'

is_win = False
for i in world_champions.values():
    if i == country:
        is_win = True
if is_win == True:
    print(f"{country} cтановилась чемпионом мира по футболу в 21 веке!")
else:
    print(f"{country} не cтановилась чемпионом мира по футболу в 21 веке!")
