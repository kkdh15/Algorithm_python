# 2798
# num, m = map(int, input().split())
# num_lst = list(map(int, input().split()))
# answer = 0

# for i in range(num):
#     for j in range(i+1, num):
#         for k in range(j+1, num):
#             answer_lst = []
#             answer_lst.append(num_lst[i])
#             answer_lst.append(num_lst[j])
#             answer_lst.append(num_lst[k])
#             if sum(answer_lst) <= m:
#                 answer = max(sum(answer_lst), answer)
# print(answer)

# 2231
# decompose = list(input())
# num_decompose = int("".join(decompose))
# answer_lst = []

# for i in range(1, num_decompose):
#     num_constructor = 0
#     num_constructor += i
#     str_constructor = []
#     while(num_constructor != 0):
#         str_constructor.append(str(num_constructor % 10))
#         num_constructor = num_constructor // 10
#     num_constructor += i
#     for j in range(len(str_constructor)):
#         num_constructor += int(str_constructor[j])
#     if num_constructor == num_decompose:
#         answer_lst.append(i)

# if len(answer_lst) == 0:
#     print(0)
# else:
#     print(min(answer_lst))

# 천잰가 이새끼?
# n = int(input())
# print([*[i for i in range(n)if n == i+sum(map(int, str(i)))], 0][0]) // [*[1,2,3],0] -> [1,2,3,0]

#  7568
# N = int(input())
# people = []

# for i in range(N):
#     people.append([1, *map(int, input().split())])

# for i in people:
#     for j in people:
#         if (i[1] < j[1]) & (i[2] < j[2]):
#             i[0] += 1
#     print(i[0], end=" ")


# 1018
# n, m = map(int, input().split())
# chess = []

# for i in range(n):
#     chess.append(input())

# bw_list = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
#            'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'] * 4
# wb_list = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
#            'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'] * 4

# res = 64
# for row in range(n-7):
#     for col in range(m-7):
#         my_list = []
#         cnt_bw = 0
#         cnt_wb = 0
#         for i in range(row, row+8):
#             for j in range(col, col+8):
#                 my_list.append(chess[i][j])
#         for i in range(64):
#             if my_list[i] != bw_list[i]:
#                 cnt_bw += 1
#             if my_list[i] != wb_list[i]:
#                 cnt_wb += 1
#         res = min(res, cnt_bw, cnt_wb)
# print(res)
# 1018
n, m = map(int, input().split())
chess = []

for i in range(n):
    chess.append(input())

res = 64
for row in range(n-7):
    for col in range(m-7):
        cnt = 0
        for i in range(row, row+8, 2):
            for k in range(col, col+8, 2):
                if chess[i][k] != 'W':
                    cnt += 1
            for k in range(col+1, col+8, 2):
                if chess[i][k] != 'B':
                    cnt += 1
        for i in range(row+1, row+8, 2):
            for k in range(col, col+8, 2):
                if chess[i][k] != 'B':
                    cnt += 1
            for k in range(col+1, col+8, 2):
                if chess[i][k] != 'W':
                    cnt += 1
        sum = min(cnt, 64-cnt)
        res = min(res, sum)
print(res)

# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB

# 1436
# N = int(input())
# 0~5 666
# 666 0~9
# 7~9 666
# 1~5 666 0~9
# 666 00~99
# 7~9 666 0~9
