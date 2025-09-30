a = list(input().split('('))

if len(a) == 1:
    print(a[0])
    print('-')
else:
    print(a[0])
    print(a[1][:len(a[1]) - 1])