# # 2609
# a, b = map(int, input().split())
# max_num = 0

# for i in range(1, a+1):
#     if (a % i == 0) & (b % i == 0):
#         max_num = max(i, max_num)
# print(max_num)
# print((a//max_num)*(b//max_num)*max_num)

# 1934


# N = int(input())


# def gcd(a, b):
#     if a > b:
#         while b > 0:
#             a, b = b, a % b
#         return a
#     else:
#         while a > 0:
#             b, a = a, b % a
#         return b


# for i in range(N):
#     a, b = map(int, input().split())
#     num = gcd(a, b)
#     print(a//num*b//num*num)

# 6588
# import sys 시간ㄱ초과!

# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True


# while True:
#     goldbach = int(sys.stdin.readline().rstrip())
#     if goldbach == 0:
#         break
#     flag = 0
#     for i in range(goldbach//2, 1, -1):
#         if isPrime(i) & isPrime(goldbach-i):
#             print(f'{goldbach} = {i} + {goldbach-i}')
#             flag = 1
#             break
#     if flag == 0:
#         print("Goldhach's conjecture is wrong.")

# import sys

# num = 1000001
# arr = [True for _ in range(num)]
# for i in range(2, int((num-1)**0.5)+1):
#     if arr[i]:
#         for k in range(i+i, num, i):
#             arr[k] = False

# while True:
#     n = int(sys.stdin.readline())

#     if n == 0:
#         break

#     flag = 0

#     for a in range(3, len(arr)):
#         if arr[a] and arr[n-a]:
#             print(str(n) + " = " + str(a) + " + " + str(n-a))
#             flag = 1
#             break
#     if flag == 0:
#         print("Goldbach's conjecture is wrong.")

# 1676
# def fac(num):
#     if num == 0:
#         return 1
#     else:
#         return num * fac(num-1)


# N = int(input())
# str_fac = str(fac(N))
# cnt = 0
# for i in range(len(str_fac)-1, 0, -1):
#     if str_fac[i] == '0':
#         cnt += 1
#     else:
#         break
# print(cnt)

# 2004
# N, M = map(int, input().split())


# def count_number(n, k):
#     count = 0
#     while n:
#         n //= k
#         count += n
#     return count


# five_count = count_number(N, 5) - count_number(M, 5) - count_number(N - M, 5)
# two_count = count_number(N, 2) - count_number(M, 2) - count_number(N - M, 2)

# answer = min(five_count, two_count)
# print(answer)
