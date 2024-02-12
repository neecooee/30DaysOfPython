empty_tuple = ()
empty_tuple = tuple()

tp1 = ('item1', 'item2', 'item3')

fruits = ('banana', 'orange', 'mango', 'lemon')
len(fruits)

first = fruits[0]
all = fruits[0:4]
all = fruits[0:]
middle_two = fruits[1:3]
aslst = list(fruits)
print('orange' in fruits)
print('aple' in fruits)

#cant do fruits[0] = 'apple'

tp3 = tp1 + fruits #only way to append to a tuple
del tp1

#slice by convertng to a list and then removing an index