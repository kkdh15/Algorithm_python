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
N = int(input())
people = []

for i in range(N):
    people.append([1, *map(int, input().split())])

for i in people:
    for j in people:
        if (i[1] < j[1]) & (i[2] < j[2]):
            i[0] += 1
    print(i[0], end=" ")
