>>> tuple1 = ('a', 'z', 'c')
>>> tuple1[0] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> tuple1.append('x')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError:'tuple' object has no attribute 'append'
>>> tuple1.index('z')
1
>>> () == True
False