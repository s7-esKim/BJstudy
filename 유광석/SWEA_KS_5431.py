import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for ts in range(1):
    tot, fin = map(int, input().split())
    stu = list(map(int, input().split()))
    good_stu = [0] * tot
    # 제출한 학생들 번호를 좋은 학생리스트에 인덱스에 맞게 넣어줌
    for i in stu:
        good_stu[i-1] = i # 리스트가 0부터 시작하므로 인덱스 맞추기
    ans = []
    print(good_stu)
   # 값이 0인 나쁜 학생을 인덱스로 접근해서 찾은 후 ans에 추가
    for i in range(tot):
        if good_stu[i] == 0:
            ans.append(i+1)
    # 언팩으로 출력
    print(f'#{ts+1}', *ans)
