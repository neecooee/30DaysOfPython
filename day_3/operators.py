age = 20
height = 6.020
comp = 1 + 3j
#base = input('Enter Trainge Base: ')
#height = input('Enter Triane Height: ')

#print(int(0.5 * ((int(base) * int(height)))))

# Given equation: y = 2x - 2

# Slope (m)
slope = 2

# Y-intercept (b)
y_intercept = -2

# X-intercept (set y to 0 and solve for x)
x_intercept = -y_intercept / slope

# Y-intercept (set x to 0 and solve for y)
y_intercept_value = slope * 0 + y_intercept

# Print the results
print("Slope (m):", slope)
print("Y-intercept (b):", y_intercept)
print("X-intercept:", x_intercept)
print("Y-intercept value:", y_intercept_value)


print(('on' in 'python') and ('on' in 'dragon'))

sentence = 'I hope this course is not full of jargon.'

print('jargon' in sentence)

print(('on' not in 'python') and ('on' not in 'dragon'))

p = 'python'

len_p = len(p)

print(len(p))
print(float(len_p))

print(60 % 2 == 0)
print(7 // 3 == 2)
print(type('10') == type(10))
print(int(float('9.8')) == 10)

hours = float(input('Enter hours: '))
rate = float(input('Enter rate per hour: '))

print('your weekly earnings is ', int((rate * hours)))

for i in range(1, 6):
    print(i, 1, i**2, i**3)