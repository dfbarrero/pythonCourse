#!/usr/bin/python

a, b = 0, 1 # Init variables
print("a = ", a)

while b < 10: # This is a loop
	print("b = ", b)  # Identation is very important here!
	a, b = b, a+b
