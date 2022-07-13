# # 2750
# sort 쓴 경우
# num = int(input())
# lst = []
# for i in range(num):
#     lst.append(int(input()))
# lst.sort()
# for i in lst:
#     print(i)
# ---------------------------------
# sort 안 쓸 때

# N = int(input())
# lst = []
# for i in range(N):
#     lst.append(int(input()))

# for i in range(len(lst)):
#     for j in range(i, len(lst)):
#         if lst[i] > lst[j]:
#             # a = lst[j]
#             # lst[j] = lst[i]
#             # lst[i] = a
#             lst[j], lst[i] = lst[i], lst[j]
# for i in lst:
#     print(i)

# 2751
# import sys
# n = int(input())
# li = []
# for _ in range(n):
#     li.append(int(sys.stdin.readline()))
# for i in sorted(li):
#     print(i)

# 10989
# import sys
# N = int(sys.stdin.readline())

# counting_lst = [0] * 10001
# for i in range(N):
#     counting_lst[int(sys.stdin.readline())] += 1

# for i in range(10001):
#     for j in range(counting_lst[i]):
#         print(i)

# 2108
# from collections import Counter
# import sys
# N = int(sys.stdin.readline())
# lst = []

# for i in range(N):
#     lst.append(int(sys.stdin.readline()))

# print(round(sum(lst)/N))
# lst.sort()
# print(lst[N//2])
# cnt = Counter(lst).most_common(2)

# if len(lst) > 1:
#     if cnt[0][1] == cnt[1][1]:
#         print(cnt[1][0])
#     else:
#         print(cnt[0][0])
# else:
#     print(cnt[0][0])
# print(max(lst)-min(lst))

# 1427
# N = input()
# lst = []
# for i in N:
#     lst.append(int(i))
# lst.sort(reverse=True)

# for i in lst:
#     print(i, end="")

# 11650
# N = int(input())
# lst = []
# for i in range(N):
#     lst.append(list(map(int, input().split())))
# lst.sort(key=lambda x: (x[0], x[1]))
# for i in lst:
#     print(i[0], i[1])

# 11651
# N = int(input())
# lst = []
# for i in range(N):
#     lst.append(list(map(int, input().split())))
# lst.sort(key=lambda x: (x[1], x[0]))
# for i in lst:
#     print(i[0], i[1])

# 1181
# N = int(input())
# lst = []

# for i in range(N):
#     lst.append(input())
# lst = list(set(lst))
# lst.sort(key=lambda x: (len(x), x))
# for i in lst:
#     print(i)

# 10814
# N = int(input())
# lst = []
# for i in range(N):
#     lst.append(input().split())
# lst.sort(key=lambda x: int(x[0]))
# for i in lst:
#     print(i[0], i[1])

# 18870
import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

dic = list(set(lst))
dic.sort()

xy = {}
for i in range(len(dic)):
    xy[dic[i]] = i

for i in lst:
    print(xy[i], end=' ')
