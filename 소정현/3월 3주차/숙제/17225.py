'''
손님들은 파란색 포장지를 원하면 상민이에게, 빨간색 포장지를 원하면 지수에게 주문
상민이는 A초, 지수는 B초
두 사람이 동시에 선물을 가져올 때는 알바짬이 조금 더 있는 상민이가 먼저 가져오고,
지수가 그 뒤의 선물을 가져온다.
손님의 수와 각 손님이 주문한 시각, 선택한 포장지, 포장 받을 선물의 개수가 주어졌을 때
상민이와 지수가 각자 어떤 선물들을 포장했는지 알아내는 프로그램을 작성해보자.

첫 줄에 상민이가 선물 하나를 포장하는 데 걸리는 시간 A,
지수가 선물 하나를 포장하는 데 걸리는 시간 B, 어제 세훈이 가게의 손님 수 N(1 ≤ N ≤ 1,000)이 주어진다.

이후 N개의 줄에 걸쳐 1번부터 N번 손님의 주문 시각 ti(1 ≤ ti ≤ 86,400),
선택한 포장지의 색깔 ci(ci = "B"|"R"), 주문한 선물의 개수 mi(1 ≤ mi ≤ 100)가 주어진다.

ti는 가게가 오픈한 지 ti초 후에 손님이 주문했음을 뜻하며 ci는 포장지의 색깔을 의미하는
알파벳으로 "B"는 파란색을, "R"은 빨간색을 의미한다.
주어지는 입력은 시간의 흐름에 맞게 ti의 오름차순으로 주어지며, 서로 같은 시간에 주문한 손님은 없다.

'''
from collections import deque

A, B, N = map(int,input().split())
second_q = deque()
color_q = deque()
tot_q = deque()

for n in range(N):
    second, color, tot = input().split()
    second_q.append(int(second))
    color_q.append(color)
    tot_q.append(int(tot))

visit = [0] * sum(tot_q)
time = 0
cnt = 0

while cnt != sum(tot_q):
    time += 1
