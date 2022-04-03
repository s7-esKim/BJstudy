import sys
sys.stdin = open('배.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    crane = list(map(int, input().split()))
    m = int(input())
    weight = list(map(int, input().split()))

    crane.sort(reverse=True)
    weight.sort(reverse=True)

    if max(weight) > max(crane):
        print(-1)
    else:
        result = 0
        while True:
            if len(weight) == 0:
                break
            for i in range(len(crane)):
                for j in range(len(weight)):
                    if crane[i] >= weight[j]:
                        weight.pop(j)
                        break
            result += 1
    print(result)