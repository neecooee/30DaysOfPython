newlist = [expression for item in iterable if condition == True] 
#this is the whole idea of what list comprehension is

'''numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers_filter = [i for i in numbers if i <= 0]
print(numbers_filter)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]
print(flattened)

tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuple_list)'''

'''countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


output = [[country.upper(), country[:3].upper(), city] for sublist in countries for country, city in sublist]

print(output)

output = [{'country': country.upper(), 'city': city} for sublist in countries for country, city in sublist]

print(output)'''


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

output = [first + ' ' + last for sublist in names for first, last in sublist]

print(output)