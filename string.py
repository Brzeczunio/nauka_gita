a='ala ma kota'
print(a)
a=u'ala ma kota'
print(a)
a='ala'+'ma'+'kota'
print(a)
print(len(a))
if(a[:1]=='a'):
    print(a[-4])
else:
    print('No nie za brdzo')

print('{0}, {1}, {2}'.format(*'abc'))

a = 'Psa'

print('%s ma %s' % (a,a))
