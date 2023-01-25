from StrKeyDict import StrKeyDict0

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
print(d.get('2'))
print(d.get(4))
print(d.get(1, 'N\A'))
print(2 in d)
print(1 in d)