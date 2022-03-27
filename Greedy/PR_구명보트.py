def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people)- 1
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1

    return answer
    
# 투포인터와 같은 논리로 풀었다 
# 앞과 뒤로 포인터를 두고 최대 2명이라는 점을 이용해 가장 작은 무게의 사람과 가장 무거운 무게의 사람을 더해서 하나의 구명보트로 count
