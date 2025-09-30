import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/16934


class Node(object):
    def __init__(self, key, data=None):
        self.key = key #값으로 입력될 문자
        self.data = data #문자열의 종료를 알리는 flag
        self.children = {} #자식노드를 저장

class Trie:
    def __init__(self): #head를 빈 노드로 저장
        self.head = Node(None)
        self.nickname_count = {}  # 닉네임별 등장 횟수

    def insert(self, string): #트리를 생성하는 함수
        current_node = self.head #self.head라는 존재하는 - 클래스 선언시에 자동으로 만들어지는 - 객체와 currnet_node를 얕은 복사

        for char in string: 
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string): #문자열이 존재하는지에 대한 여부를 리턴하는 함수입니다. 문자열을 하나씩 돌면서 확인 후 ​마지막 노드가 data가 존재한다면 True를, 그렇지 않거나 애초에 children에 존재하지 않는다면 False를 리턴합니다.
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix): #prefix단어로 시작하는 단어를 찾고 배열로 리턴하는 함수입니다. prefix단어까지 tree를 순회 한 이후 그다음부터 data가 존재하는 것들만 배열에 저장​하여 리턴합니다.
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return False

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                    break #접두사가 겹치는 단어가 하나라도 있다면 끝
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words
    


t = int(input())

trie = Trie()

for _ in range(t):
    temp = input().strip()
    shortest_t = temp
    
    for x in range(len(temp)):
        if trie.starts_with(temp[0:x + 1]) == False:
            shortest_t = temp[0 :x + 1]
            break
        else:
            pass
    
    ans_t = shortest_t
    # print(shortest_t, 'n')

    
    
    if temp in trie.nickname_count:
        trie.nickname_count[temp] += 1
        ans_t = temp + str(trie.nickname_count[temp])
    else:
        trie.insert(temp)
        trie.nickname_count[temp] = 1
       
    
    print(ans_t)
        
    

