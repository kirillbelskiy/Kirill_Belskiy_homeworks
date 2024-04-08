d = {'key1': 'value1'}

d['key2'] = 100

d[('key3',)] = ['value3']

print(d['key1'])

d.pop('key1')

keys = list(d.keys())
print(keys)
