number = int(input('Enter a number: '))

if number > 1:
	is_prime = True
	for divider in range(2, number):
		if number % divider == 0:
			is_prime = False
			break
else:
	is_prime = False
	
if is_prime:
	print('The number {0} is prime.' .format(number))
else:
	print('The number {0} not is prime.' .format(number))
