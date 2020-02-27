def fib(n):
    """Print a Fibonacci series up to n """
    result = [] # Declare a new list
    a, b = 0, 1
    while a < n:
    	result.append(a) # Add to the list
    	a, b = b, a+b
    return result
