#Day 2: Days of python programming

firstname = 'Nick'
lastname = 'Cyr'

fullname = firstname + ' ' + lastname
age = 20
is_married = False

fav_color, fav_exercise, bench_max = 'red', 'lateral raise', 225


print(fullname)
print(len(firstname))

r = 30
pi = 3.14

area_of_circle = pi *(30 ** 2)
print(area_of_circle)

circum_of_circle = ((2 * pi) * r)
print(circum_of_circle)

first_name = input('What is your name: ')
last_name = input('What is your last name: ')
country = input('where are you from: ')
person_age = input('how old are you: ')

person_attr = {
    'first' : first_name,
    'last' : last_name,
    'country' : country,
    age : int(person_age)
}

print(person_attr)