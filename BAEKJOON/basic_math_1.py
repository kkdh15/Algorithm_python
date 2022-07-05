# 1712
# fixed_cost, variable_cost, sales = map(int, input().split())
# benefit = sales - variable_cost
# count = 0
# if(benefit <= 0):
#     print(-1)
# else:
#     count = (fixed_cost // benefit) + 1
#     print(count)

# 2292
# num = int(input())
# cnt = 0
# if num == 1:
#     print(1)
# else:
#     for i in range(1, num):
#         cnt += i*6
#         if(cnt >= num-1):
#             print(i+1)
#             break

# 1193
# num = int(input())
# cnt = 0
# res = 0
# if num == 1:
#     print("1/1")
# elif num == 2:
#     print("1/2")
# else:
#     for i in range(1, num):
#         cnt += i
#         if(cnt >= num):
#             res = i
#             break
#     index = 0
#     for i in range(1, res):
#         index += i

#     sum = num - index
#     if res % 2 == 0:
#         print(str(sum)+"/"+str(res+1-sum))
#     else:
#         print(str(res+1-sum)+"/"+str(sum))

# 10757
# a, b = map(int, input().split())
# print(a+b)

# 2869
# a, b, v = map(int, input().split())
# height = v - a
# day = 1
# if height >= (a-b):
#     day += height // (a-b)
# if (height % (a-b) > 0):
#     day += 1
# print(day)

# 2839
# num = int(input())
# cnt_t = 0
# cnt_f = 0
# sum = -1

# if num % 5 == 0:
#     sum = num // 5
# elif (num % 3 == 0) & (num < 15):
#     cnt_t = num // 3
#     cnt_f = 0
#     sum = cnt_t + cnt_f
# else:
#     for i in range((num//5)+1):
#         if (num - i*5) % 3 == 0:
#             cnt_f = i
#             cnt_t = (num-i*5) // 3
#             sum = cnt_t + cnt_f
# print(sum)

# 2775
# def solve(k, n):
#     cnt = 0
#     if k == 0:
#         return n
#     else:
#         for i in range(1, n+1):
#             cnt += solve(k-1, i)
#     return cnt


# num = int(input())
# for i in range(num):
#     k = int(input())
#     n = int(input())
#     print(solve(k, n))

# 2774 better way
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     k = int(input())
#     n = int(input())

#     people = [i for i in range(n + 1)]
#     for i in range(k):
#         for j in range(1, n + 1):
#             people[j] = people[j] + people[j - 1]

#     print(people[-1])

# 10250
num = int(input())
for i in range(num):
    h, w, n = map(int, input().split())
    if n % h == 0:
        floor = h
        room_number = n // h
    else:
        floor = n % h
        room_number = (n // h) + 1
    print('{}{:0>2}'.format(floor, room_number))
