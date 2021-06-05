a = {}
b = {}

a['um'] = 'primeiro'

print(a)

a['dois'] = 'segundo'

print(a)

b['recebe'] = a
print(b)

a['recebe'] = {'1':'1'}
print(b)