# S --> T 다음과 같이 짤 경우 메모리 초과 뜸
# from collections import deque
# s = input()
# t = input()
# l = deque()
# l.append(s)
# while len(l[0]) < len(t):
#     now = l.popleft()
#     l.append(now+'A')
#     l.append(now[::-1] + 'B')

# change = False
# for i in l:
#     if i == t:
#         change = True
#         break

# if change:
#     print(1)
# else:
#     print(0)

# T --> S로 맨 뒤만 점검하는 방식으로 가야 메모리초과도 시간초과도 안뜸
# 또한 문자열을 리스트로 바꾸는 것이 뒤집고 원소를 제거하기에 유리하다.

s = list(input())
t = list(input())

switch = False
while t:
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()
    if s == t:
        switch = True
        break

if switch:
    print(1)
else:
    print(0)
        
