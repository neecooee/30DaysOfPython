'''\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
'''
'''
t = 'Thirty'
d = 'Days'
o = 'Of'
p = 'Python'
sp = ' '
print(t + sp + d + sp  + o + sp + p)
'''

'''company = 'Coding For All'
print(len(company))

print(company.upper())
print(company.lower())
print(company.title())
print(company.swapcase())
print(company.capitalize())
print(company[7:])
print(company.startswith('Coding'))
print(company.index('Coding'))
print(company.replace('Coding', 'Counting the money for fun'))
print(company.split(' '))
print(company[0])
lastindex = len(company) - 1
print(company[lastindex]) 
print(company[10])

acronym = ''.join(word[0] for word in company.split())
print(acronym)
print(company.index('C'))
print(company.index('l'))
print(company.rfind('l'))

bc = 'you cannot end a sentence with because because because is a conjuction'

print(bc.index('because'))
print(bc.find('because'))


print(bc.replace('because because because', '').replace('  ', ' '))

ws = ' Coding For All  '
print(ws)
print(ws.strip())

#is identifier checks for valid naming

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

# Join the list with ' # ' string
joined_libraries = ' # '.join(libraries)

print(joined_libraries)'''


print('I am enjoying thischallenge.\nI just wonder what is next.')

name = 'Nick'
age = '20'
country = 'UW'
city = 'madison'

print('name\tage\tcountry\t  city\n{}\t{}\t{}\t  {}'.format(name, age, country, city))

rad = 10
area = 3.14 * (rad ** 2)
a = 4
b = 3

print(f'The area of a circle with radius {rad} is {area:.2f} meters squared')
print('{} + {} = {}'.format(a, b, a + b))