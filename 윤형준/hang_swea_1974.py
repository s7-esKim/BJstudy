import sys
sys.stdin = open('input 1974.txt')

def selection_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    onetonine = [1,2,3,4,5,6,7,8,9]

    result = 1
    for i in range(9):
        check_arr1 = []
        check_arr2 = []
        for j in range(9):
            check_arr1.append(arr[i][j])
            check_arr2.append(arr[j][i])
        check_arr1 = selection_sort(check_arr1)
        check_arr2 = selection_sort(check_arr2)
        if check_arr1 != onetonine or check_arr2 != onetonine:
            result = 0
            break


    for i in range(0,7,3):
        for j in range(0,7,3):
            check_arr3 = []
            for k in range(3):
                for l in range(3):
                    check_arr3.append(arr[k+i][l+j])
            check_arr3 = selection_sort(check_arr3)
            if check_arr3 != onetonine:
                result = 0
                break

    print(f'#{tc} {result}')

