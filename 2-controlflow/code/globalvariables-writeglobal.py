a = 5

def f():
    global a
    a = 0
    print(a)
    return

f()
print(a)