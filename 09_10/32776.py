a = int(input())

f = sum(list(map(int, input().split())))

if a <= f or a <= 4 * 60:
    print('high speed rail')
else:
    print('flight')