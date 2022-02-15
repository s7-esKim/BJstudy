import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def sort_number(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

for ts in range(T):
    N, K = map(int, input().split())
    subject_grade = list(map(int, input().split()))
    max_tot = 0
    subject_grade = sort_number(subject_grade)
    for k in range(K):
        max_tot += subject_grade[-1]
        subject_grade = subject_grade[:len(subject_grade)-1]
    print(f'#{ts+1} {max_tot}')
