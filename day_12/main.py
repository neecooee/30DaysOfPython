from random import *
import string
'''#import Modules
from Modules import generate_full_name as fullname
import sys

print(fullname('Nick', 'Cyr'))

#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base'''
'''
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2'''

'''When we import we can also rename the name of the function.

from math import pi as  PI
print(PI) # 3.141592653589793'''

'''import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

'''from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive'''

'''def random_user_id(): 
    return ''.join(choices(string.ascii_letters + string.digits, k = 6))

print(random_user_id())

def user_id_gen_by_user():
    chars = input("num chars please:")
    numids = input("num ID's please:")

    for i in range(int(numids)):
        print(''.join(choices(string.ascii_letters + string.digits, k = int(chars))))
    return 

print(user_id_gen_by_user()) 
''''''
def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())'''

'''def list_of_hexa_colors():
    arr = []
    
    n = randint(1, 10)
    letters_af = 'abcdef'
    
    while n > 0:
        str = ''.join(choices(letters_af + string.digits, k = 6))
        arr.append(str)
        n -= 1
    return arr

print(list_of_hexa_colors())'''
'''
def generate_colors(kind, ammount):
    letters_af = 'abcdef'
    
    if kind == 'hexa':
       return [''.join(choices(letters_af + string.digits, k = 6)) for _ in range(ammount)]
   
    if kind == 'rgb':
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return [f"rgb({r},{g},{b})" for _ in range(ammount)]

print(generate_colors('hexa', 6))
print(generate_colors('rgb', 6))'''

def shuffle_list(list):
    copy = list.copy()
    shuffle(copy)
    return copy

list = [1,2,3,4,5,6,7]
print(list)
print(shuffle_list(list))


'''def generate_unique_random_numbers():
    """
    Generate an array of seven unique random numbers in the range of 0-9.

    Returns:
    - List of seven unique random numbers.
    """
    unique_numbers = random.sample(range(10), 7)
    return unique_numbers

# Example usage
random_numbers = generate_unique_random_numbers()
print("Generated Unique Random Numbers:", random_numbers)'''