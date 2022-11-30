>>> tel['guido'] = 4127
>>> del tel['sape']
>>> tel
{'guido': 4127, 'jack': 4098}
>>> list(tel.keys())
['guido', 'jack']
>>> 'guido' in tel
True
