countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


output = [[country.upper(), country[:3].upper(), city] for sublist in countries for country, city in sublist]

print(output)

output = [{'country': country.upper(), 'city': city} for sublist in countries for country, city in sublist]

print(output)