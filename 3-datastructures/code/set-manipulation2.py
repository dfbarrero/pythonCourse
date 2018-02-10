set_mix1 = {'a', 'b'}
>>> set_mix1.add('c')
{'a', 'b', 'c'}
>>> set_mix1.add('a')
>>> set_mix1
{'a', 'b', 'c'}
>>> set_mix1.update({'b', 'c', 'd'}, {'b', 'e', 'a'})
>>> set_mix1
{'a', 'b', 'c', 'd', 'e'}
>>> set_mix1.update(['b', 'c', True])
>>> set_mix1
{'a', 'b', 'c', 'd', 'e', True}
>>> set_mix1.discard(False)
>>> set_mix1
{'a', 'b', 'c', 'd', 'e', True}





