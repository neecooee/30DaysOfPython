'''age = input('Enter your age: ')

if int(age) > 18:
    print('nice you can drive')
else:
    print(f'you need {18 - int(age)} more years to learn to drive.')
    
# Get your age as input
your_age = int(input("Enter your age: "))

# Predefined age (my age)
my_age = 20  # You can replace this with your actual age

# Compare ages using if...else statements
if my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f"I am 1 year younger than you.")
    else:
        print(f"I am {age_difference} years younger than you.")
elif my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print(f"I am 1 year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
else:
    print("We are the same age!")

# Output will depend on the actual ages provided.


score = 75

grade = 'A' if score >= 80 else 'B' if score >= 70 else 'C' if score >= 60 else 'D' if score >= 50 else 'F'

print(f"The student's grade is: {grade}")

# Get user input for the month
user_month = input("Enter a month: ").capitalize()  # Convert the input to capitalize first letter

# Check the season based on the input month
if user_month in ['September', 'October', 'November']:
    season = 'Autumn'
elif user_month in ['December', 'January', 'February']:
    season = 'Winter'
elif user_month in ['March', 'April', 'May']:
    season = 'Spring'
elif user_month in ['June', 'July', 'August']:
    season = 'Summer'
else:
    season = 'Invalid month entered'

# Print the result
print(f"The season for {user_month} is {season}.")


fruits = ['banana', 'orange', 'mango', 'lemon']

fruit_input = input('Enter a fruit: ')
'''

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit_input = input('Enter a fruit: ')

if not fruit_input in fruits:
    fruits.append(fruit_input)
    print(', '.join(fruits))
else:
    print('That fruit already exists in the list')
    
person= {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if person.get('skills') is not None:
    skills_list = person['skills']
    middle_index = (len(skills_list) - 1) // 2
    middle_element = skills_list[middle_index] if len(skills_list) % 2 != 0 else skills_list[middle_index:middle_index + 2]
    print("Middle element or elements:", middle_element)
    
    if 'python' in skills_list:
        print('python is one of your skills')
        
    if set(['JavaScript', 'React']).issubset(skills_list):
        print('He is a front-end developer')
    elif set(['Node', 'Python', 'MongoDB']).issubset(skills_list):
        print('He is a backend developer')
    elif set(['React', 'Node', 'MongoDB']).issubset(skills_list):
        print('He is a fullstack developer')
    else:
        print('Unknown title')
else:
    print('Skills information is missing')

if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} is married and lives in Finland.")

    
