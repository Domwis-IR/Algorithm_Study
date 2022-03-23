l = [666]
x = 667
while len(l) != 10000:
    if '666' in str(x):
        l.append(x)
    x += 1
n = int(input())
print(l[n-1])

# 아래와 같이도 풀이가 가능하다.
# 위의 경우에는 미리 리스트를 만드는 방법
# 아래의 경우에는 필요한 부분까지 찾는 방법
# n = int(input())
# cnt = 0
# six_n = 666
# while True:
#     if '666' in str(six_n):
#         cnt += 1
#     if cnt == n:
#         print(six_n)
#         break
#     six_n += 1
