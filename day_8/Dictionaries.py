'''empty_dict = {}
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    } #dicts can be nested in dicts fr

print(len(dct)) #prints number of key value pairs

print(dct['key1'])
print(dct['key4'])
print(person['skills'][0])
print(person['address']['street'])

print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

dct['key5'] = 'value5'

print('key2' in dct)
print('key6' in dct)

dct.pop('key1')
dct.popitem() #removes last item
del dct['key2']
print(dct.items()) # changes to a list of tuples
print(dct.clear())
del dict
dct_copy = dct.copy()

keys = dct.keys()
values = dct.values()

'''

dog = {}

list_for_dog = [('first', 'bailey'), ('breed', 'godlen'), ('legs', 4), ('age', 9)]
dog.update(list_for_dog)
print(dog)

student = {
    
    'first' : 'nick',
    'last' : 'cyr',
    'gender' : 'male',
    'age' : 20 ,
    'marital status' : 'gf',
    'skills' : ['python now', 'java', 'C', 'JS'],
    'country' : 'us',
    'city' : 'madtown',
    'addr' : 'yo momma st' 
    
}

print(len(student))
print(type(student.get('skills')))
student.get('skills').append('sudoku') #add only for sets
print(student)

l = list(student.keys())
print(l)
print(student.items())
del student['marital status']
print(student.items())

del dog
print(dog)