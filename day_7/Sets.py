'''st  = set()
st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}

len(fruits)
'banana' in fruits
fruits.add('apple')
st.update(['item5','item6','item7'])
st.update(fruits)
st.remove('item4')
fruits.pop() # remove random from a set
st.clear()
del fruits

lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst) 

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}

even_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}'''

#################################Exercises Day 7######################
# sets
#it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
'''
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies) #unordered so wont be added to end

it_companies.update(['UW', 'Anita'])
print(it_companies) 

it_companies.remove('Oracle')
it_companies.pop()
print(it_companies) #pop chose a random to remove

it_companies.discard('Apple')
print(it_companies)'''

C = A.union(B)
A.update(B)
print(C)
print(A)

print(A.issubset(B))
print(A.isdisjoint(B)) #all different between A and B
print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A
del B