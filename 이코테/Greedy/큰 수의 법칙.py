n, m, k = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

answer = 0
answer += n_list[-1]*k
cnt = k
while cnt != m:
    if cnt % k == 0:
        if n_list[-2] != n_list[-1]:
            answer += n_list[-2]
            cnt += 1
        else:
            answer += n_list[-1]
            cnt += 1
    else:
        answer += n_list[-1]
        cnt += 1
print(answer)
