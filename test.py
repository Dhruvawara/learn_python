for i in range(0, 5):
    if i in (0, 4):
        i = 3
    print('*', ' '.join(['*'] * (i+1)).rjust(7, ' '),
          ' '.join(['$'] * (i+1)).ljust(7, ' '), '$')

for i in range(4, -1, -1):
    i = abs(i)
    if i in (0, 4):
        i = 3
    print('@', ' '.join(['@'] * (i+1)).rjust(7, ' '),
          ' '.join(['#'] * (i+1)).ljust(7, ' '), '#')
