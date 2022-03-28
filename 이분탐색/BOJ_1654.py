n,k = map(int,input().split())
l = [int(input()) for _ in range(n)]
start, end = 1, max(l)
while start <= end:
    mid = (start+end) // 2
    lines = 0
    for i in l :
        lines += i // mid
    if lines  >= N:
        start = mid + 1
    else:
        end = mid -1
print(end)
