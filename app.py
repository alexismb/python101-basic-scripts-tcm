#num1 = input('Enter your first number: ')
#num2 = input('Enter your second number: ')
#sum = float(num1) + float(num2)
#print(num1 + ' + ' + num2 + ' = ' + str(sum))

weight = float(input('Weight: '))
unit = input('(L)bs or (K)gs')
if unit.upper() == 'L':
    converted = weight * 0.45
    print('Your weight in Kg is:' + str(converted))
else: 
    converted = weight / 0.45
    print('Your weight in Lbs is:' + str(converted))
