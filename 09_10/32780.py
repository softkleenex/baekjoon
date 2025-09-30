from math import pow
import itertools
from collections import Counter

lv = int(input())


x = (pow(10, 9) + 7)

if lv <= 5:
    print(pow(4, lv) // x)
else:
    ans = 0
    if lv == 6:
        list1 = [i for i in range(0, 8)]
        list2 = [i for i in range(8, 16)]
        for rv in range(0, 6 + 1):
            
            combinations1 = itertools.combinations_with_replacement(list2, rv)
            flattened1 = [item for combo in combinations1 for item in combo]
            
            combinations2 = itertools.combinations_with_replacement(list1, lv - rv)
            flattened2 = [item for combo in combinations2 for item in combo]
            
            counter1 = Counter(flattened1)
            counter2 = Counter(flattened2)
            
            print(f"rv={rv}:")
            print("  각 원소 사용 빈도1:", counter1)
            print("  각 원소 사용 빈도2:", counter2)

           
            
    print(ans % x)
            
    