a = 5

def f():
    global a
    a = a - 1
    return

f()
print(a) 
