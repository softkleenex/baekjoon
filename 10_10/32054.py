import sys
from functools import lru_cache
sys.setrecursionlimit(100000)
input = sys.stdin.readline
print = sys.stdout.write

while 1:
    n = int(input())
    if n == 0:
        break
    
    p = []
    ally_indices = []
    enemy_indices = []
    ally_count = 0
    
    for i in range(n):
        a, b = input().split()
        prob = float(b)
        if a == 'Ally':
            p.append((1, prob))
            ally_indices.append(i)
            ally_count += 1
        else:
            p.append((0, prob))
            enemy_indices.append(i)
    
    # 팀별 비트마스크 미리 계산
    ally_mask = sum(1 << i for i in ally_indices)
    enemy_mask = sum(1 << i for i in enemy_indices)
    
    # 캐시를 위해 전역 변수로 설정
    _p = p
    _ally_mask = ally_mask
    _enemy_mask = enemy_mask
    _n = n
    _ally_indices = ally_indices
    
    @lru_cache(maxsize=None)
    def dp(phase, alive_mask):
        # 종료 조건: 모든 phase 완료
        if phase == _n:
            # 빠른 체크: 아군이 모두 살아있는지 (비트 연산)
            return 1.0 if (alive_mask & _ally_mask) == _ally_mask else 0.0
        
        # 현재 플레이어가 죽었으면 스킵
        if not (alive_mask & (1 << phase)):
            return dp(phase + 1, alive_mask)
        
        team, prob = _p[phase]
        
        # 타겟 찾기 - 비트 연산으로 최적화
        if team == 1:  # 아군
            target_mask = alive_mask & _enemy_mask
        else:  # 적군
            target_mask = alive_mask & _ally_mask
        
        # 타겟이 없으면 스킵
        if target_mask == 0:
            return dp(phase + 1, alive_mask)
        
        # 타겟 리스트 생성 - 비트에서 직접 추출
        targets = []
        temp_mask = target_mask
        while temp_mask:
            i = (temp_mask & -temp_mask).bit_length() - 1
            targets.append(i)
            temp_mask ^= (1 << i)
        
        # 확률이 극단적인 경우 최적화
        if prob < 1e-9:
            return dp(phase + 1, alive_mask)
        elif prob > 1 - 1e-9:
            if team == 1:
                return max(dp(phase + 1, alive_mask ^ (1 << t)) for t in targets)
            else:
                return sum(dp(phase + 1, alive_mask ^ (1 << t)) for t in targets) / len(targets)
        
        if team == 1:  # 아군 - 최적의 타겟 선택
            best_prob = 0.0
            miss_result = None  # 캐시
            for t in targets:
                new_mask = alive_mask ^ (1 << t)
                hit_result = dp(phase + 1, new_mask)
                if miss_result is None:
                    miss_result = dp(phase + 1, alive_mask)
                result = prob * hit_result + (1 - prob) * miss_result
                if result > best_prob:
                    best_prob = result
                    if best_prob > 0.9999:  # 거의 확실하면 조기 종료
                        break
            return best_prob
        else:  # 적군 - 랜덤 선택
            miss_result = dp(phase + 1, alive_mask)
            total_prob = 0.0
            for t in targets:
                new_mask = alive_mask ^ (1 << t)
                hit_result = dp(phase + 1, new_mask)
                result = prob * hit_result + (1 - prob) * miss_result
                total_prob += result
            return total_prob / len(targets)
    
    initial_mask = (1 << n) - 1
    ans = dp(0, initial_mask)
    
    # 캐시 클리어
    dp.cache_clear()
    
    print(f"{ans:.12f}\n")