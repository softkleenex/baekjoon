import sys
input = sys.stdin.readline

n, m = map(int, input().split())

info = dict()

for i in range(n + m):
    parent, name, isFolder = input().split()
    isFolder = int(isFolder)
    if isFolder == 1 and not(name in info):
        info[name] = []
        
    
    
    try:
        info[parent].append((name, isFolder))
    except:
        info[parent] = [(name, isFolder)]


# print(info)


q = int(input())
    

    
for i in range(q):
    query = list((input().strip().split('/')))
    # print(query)
    
    now = query[-1]

    def dfs(folder):
        filetype, filec = set(), 0                
        def  _dfs(folder):
            nonlocal filetype, filec  # 외부 변수 직접 수정
            
            if folder not in info:  # 추가 필요!
                return
            for name, isFolder in info[folder]:
                if isFolder == 1:
                    pass
                    _dfs(name)
                else:
                    filetype.add(name)
                    filec += 1
                    
        _dfs(folder)
        return len(filetype), filec

        
    a, b = dfs(now)
    print(a, b)
    
    
# print(query)

