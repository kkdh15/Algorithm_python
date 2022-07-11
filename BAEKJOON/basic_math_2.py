# 1978
# num = int(input())
# prime_number = list(map(int, input().split()))
# sum = 0

# for number in prime_number:
#     cnt = 0
#     for i in range(1, number):
#         if number % i == 0:
#             cnt += 1
#     if cnt == 1:
#         sum += 1
# print(sum)

# 2581
# start = int(input())
# end = int(input())
# number_list = [i for i in range(start, end+1)]
# prime_number = []
# for number in number_list:
#     cnt = 0
#     for i in range(1, number):
#         if number % i == 0:
#             cnt += 1
#     if cnt == 1:
#         prime_number.append(number)
# if len(prime_number) == 0:
#     print(-1)
# else:
#     print(sum(prime_number))
#     print(min(prime_number))

# 11653
# num = int(input())
# i = 2
# if num == 1:
#     print("")
# else:
#     while(i <= num):
#         if num % i == 0:
#             print(i)
#             num = num // i
#         else:
#             i += 1

# 1929
# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True


# start, end = map(int, input().split())

# for i in range(start, end+1):
#     if isPrime(i):
#         print(i)

# 4948
# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True


# while True:
#     num = int(input())
#     if num == 0:
#         break
#     cnt = 0
#     for i in range(num+1, (num*2)+1):
#         if isPrime(i):
#             cnt += 1
#     print(cnt)

# 9020
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


num = int(input())
for _ in range(num):
    goldbach = int(input())
    for i in range(goldbach//2, 1, -1):
        if isPrime(i) & isPrime(goldbach-i):
            print(i, goldbach-i)
            break
