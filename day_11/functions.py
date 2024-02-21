'''def add_two_nums(a , b):
    return a + b

print(add_two_nums(3, 4))

def area_circle(r):
    return 3.14 * (r ** 2)

print(area_circle(4))

'''

'''def add_all_nums(*nums):
    t = 0
    for n in nums:
        t += n
    return t

print(add_all_nums(4,3,5,6,7,8,9,20))'''
'''
def c_c_t_f(temp):
    return (temp * 9/5) + 32

print(c_c_t_f(10))

def check_szn(month):
    if month in ['Jan', 'Feb', 'Mar']:
        return 'Winter'
    
print(check_szn('Jan'))'''

    

def print_list(list):
    for i in list:
        print(i)
    return 'meow'
    

print(print_list(['1','2','3']))

def capitalize_list_items(list):
    capitalized_list = []

    for items in list:
        capitalized_list.append(items.capitalize())
    return capitalized_list

print(capitalize_list_items(['ab', 'bc', 'cd']))

def sum_of_nums(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum

print(sum_of_nums(100))

def evens_and_odds(num):
    num_evens = 0
    num_odds = 0
    for i in range(num + 1):
        if ((i % 2) == 0):
            num_evens += 1
        if ((i % 2) != 0):
            num_odds += 1
    print(f"The number of odds are {num_odds}\nThe number of evens are {num_evens}")

print(evens_and_odds(100))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return num * factorial(num - 1)
print(factorial(5))

def are_all_unique(my_list):
    return len(my_list) == len(set(my_list))

# Example usage:
unique_list = [1, 2, 3, 4, 5]
non_unique_list = [1, 2, 2, 3, 4, 5]

print("Are all items unique?", are_all_unique(unique_list))  # Output: True
print("Are all items unique?", are_all_unique(non_unique_list)) 