names = list()
print('変更前のlistのidentity:{}'.format(id(names)))
names.append('松田')
print('変更後のlistのidentity:{}'.format(id(names)))

name = '松田'
print('変更前のstrのidentity:{}'.format(id(name)))
name = 'スパー' + name
print('変更後のstrのidentity:{}'.format(id(name)))