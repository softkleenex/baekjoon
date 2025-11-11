import sys
input = sys.stdin.readline
def kmp(all_string, pattern):
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
            
    # #kmp
    # result = []
    # i = 0
    # for j in range(len(all_string)):
    #     while i > 0 and pattern[i] != all_string[j]:
    #         i = table[i - 1]
    #     if pattern[i] == all_string[j]:
    #         i += 1
    #         if i == len(pattern):
    #             result.append(j - i + 1)
    #             i = table[i - 1]
                
    return table




c = 1

while(1):

    t = int(input().strip())
    if t == 0:
        break
    
    
    s = input().strip()
    print(f"Test case #{c}")
    c += 1
    ans = kmp(s, s)
    # print(ans)
    
    for i, v in enumerate(ans):
        if ans[i] > 0:  # failure 값이 0보다 클 때만 
            period_len = (i + 1) - ans[i]  # 현재 인덱스의 failure 값 사용
            if (i + 1) % period_len == 0:  # 완전한 주기인지 확인
                period_freq = (i + 1) // period_len
                print(period_len * period_freq, period_freq)
    print()