#functions can be passed in as params, returning functions from other functions 

#closures allow a nested function to access outer scope of the encosing funciton
#decorators allow users to add new functionality to an existing object without modifying the structure
#map() takes a function and iterable as parameters
#filter() calls the specified function which returns boolean for each of the specified iterable(list)
#reduce() import functools needed, returns a single value

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def country_print(countries):
        print(countries + " Map")
        
def uppercase_countries(countries):
    return countries.upper()

def filter_land(countries):
    return 'land' not in countries  

def not_six(countries):
    return len(countries) != 6 
    

countries_upper_case = map(uppercase_countries, countries)
countries_filter_land = filter(filter_land, countries)
countries_filter_six = filter(not_six, countries)

print(list(countries_upper_case))
print(list(countries_filter_land))
print(list(countries_filter_six))