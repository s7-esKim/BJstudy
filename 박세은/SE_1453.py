N = int(input())  # 손님의 수
num = list(map(int, input().split()))  # 앉고 싶어하는 자리

# list 를 set 으로 변경 하면 중복되는 숫자가 사라진다.
# 중복되는 사람 = 거절당한 사람 = list - set
num_set = set(num)
print(N - len(num_set))
