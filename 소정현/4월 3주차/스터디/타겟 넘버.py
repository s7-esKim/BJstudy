

def dfs(i, tot, n, answer, numbers, target):
    if i == n:
        if tot == target:
            answer.append(1)
        return

    dfs(i+1, tot+numbers[i], n, answer, numbers, target)
    dfs(i+1, tot-numbers[i], n, answer, numbers, target)

def solution(numbers, target):
    answer = []
    dfs(0, 0, len(numbers), answer, numbers, target)
    return len(answer)

