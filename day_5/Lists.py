list_l = list()
list_2 = [1,2,3,4,5,6]
print(len(list_2))
first = list_2[0]
mid = list_2[len(list_2) // 2]
last = list_2[-1]
print(first, mid, last)
mixed_data_types = ['nick', 20, "6'0", 'gf', 'UW']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(len(it_companies))

print(it_companies[0])
print(it_companies[-1])
print(it_companies[len(it_companies) // 2])

it_companies[4] = 'UW CS'

print(it_companies)
it_companies.append("Nick's company")
print(it_companies)
it_companies.insert(4, 'Anita')
print(it_companies)
it_companies[1] = it_companies[1].upper()
print(it_companies)

s = "#; " 
s = s.join(it_companies)
print(s)

exists = 'Anita' in it_companies
print(exists)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse = True)
print(it_companies)

it_companies.remove(it_companies[len(it_companies) // 2])
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

red_in = front_end.index('Redux')
front_end.insert(red_in + 1, 'python')
front_end.insert(red_in + 2, 'SQL')
print(front_end)
