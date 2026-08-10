try:
    print('try')
    x = '' + 1
except TypeError as e:
    print(f'{e}')
else:
    print('Else block')
finally:
    print('Finally block')