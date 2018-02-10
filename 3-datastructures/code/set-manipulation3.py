>>> set_mix1.remove(False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: False
>>> set_mix1.remove(True)
>>> set_mix1
{'a', 'b', 'c', 'd', 'e'}
>>> set_mix1.pop()
'c'
>>> set_mix1
{'a', 'b', 'd', 'e'}
>>> set_mix1.clear()
>>> set_mix1
set()
>>> set_mix1 = {2, 5}
>>> set_mix2 = {1, 2, 3}
>>> set_mix1.union(set_mix2)
{1, 2, 5, 3}



