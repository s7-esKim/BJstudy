# 2 4
# C(말)AAB
# ADCB
# 상하좌호를 A = 0 B = 1 ....... 이런식으로
# # 아스키코드 65 A  ord()-65 하면 0
#
# R, C = map(int, input().split())
# board = [list(map(str, input())) for _ in range(R)]
#
# for i in range(R):
#     for j in range(C):
#         board[i][j] = ord(board[i][j]) - 65
#
# # print(board)
# visited = [0] * 26 # 총 대문자 알파벳 숫자, 지나간 알파벳에 1로 바꾸기??
# di = [-1, 1, 0, 0] # 상하좌우
# dj = [0, 0, -1, 1]
# move = 0    # 말이 지날 수 있는 최대의 칸수
#
# def dfs(i, j, cnt): # i,j는 좌표 cnt는 갈때마다 +1씩
#     global move
#     move = max(move, cnt) # 최대 칸수 초기화
#     visited[board[i][j]] = 1
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#
#         if 0 <= ni < R and 0 <= nj < C and visited[board[ni][nj]] == 0:
#             visited[board[ni][nj]] = 1
#             dfs(ni, nj, cnt+1)
#             visited[board[ni][nj]] = 0
#
#     return move
#
# dfs(0,0,1)
# print(move)
#
# # R, C = map(int, input().split())
# # board = [list(map(str, input())) for _ in range(R)]
# # visited = [[0] * C for _ in range(R)]   # 같은 곳을 다 1로 바꿔야 하는데 바꾸는 방법을 생각해보기
# # di = [-1, 1, 0, 0] # 상하좌우
# # dj = [0, 0, -1, 1]
# # move = 0
# #
# #
# # # C를 1로 바꿧으니까 index 1,2도 1로 바꿔야함
# # for i in range(R):
# #     for j in range(C):
# #         visited[i][j] = 1   # 여끼까지 0,0 1임
# #         #여기서 for문말고 C인값 찾아야하니까
# #         # ???? 방법이 생각이....우로 이동 알파벳은 달라야 이동 가능
# 알파벳번

