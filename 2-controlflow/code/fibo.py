#!/usr/bin/python

a, b = 0, 1 # Init variables

while b < 10: # This is a loop
	print("b = ", b)
	print("a = ", a)  # Identation is very important here!
	a, b = b, a+b
