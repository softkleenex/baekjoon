# https://www.acmicpc.net/problem/5670

import sys
input = sys.stdin.readline

class Node:#python3 만 사용시에 object 생략 가능
    def __init__(self, key, data = None):
        self.key = key#값으로 입력될 문자
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)#이떄 trie의 head속성이 만들어짐
        
    def insert(self, string):
        current_node = self.head#같은 객체를 가르키게 됨
        
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char] 
        current_node.data = string
        
    def searts_with(self, prefix):
        currnet_node = self.head
        words = []
   
            
        for p in prefix:
            if p in currnet_node.children:
                currnet_node = current_node.children[p]
            else:
                return False
            
        currnet_node = [currnet_node]
        next_node = []
        
        while True:
            for node in currnet_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.valude()))
                if len(next_node) != 0:
                    current_node = next_node
                    next_node = []
                else:
                    break
        
        return words
    


while True:
    try:
        n = int(input())
        words = []
        for _ in range(n):
            words.append(input())
            
    except:
        break