q = int(input())

#0 ~ 42까지 원형 연결이 있다고 하자

for i in range(q):
    a, b = map(int, (input().split())) #a에서 출발, b에 도착
    if (b - a + 43) % 43 <= (a - b + 43) % 43:
        print("Inner circle line")
    elif (b - a + 43) % 43 == (a - b + 43) % 43:
        print("Same")
    else:
        print("Outer circle line")
            