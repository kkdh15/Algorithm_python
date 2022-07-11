# 11729
# n = int(input())


# def countt(n):
#     cnt = 0
#     if n == 1:
#         cnt += 1
#         return cnt
#     else:
#         cnt += 2*countt(n-1) + 1

#         return cnt


# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, c)
#     else:
#         hanoi(n - 1, a, c, b)
#         print("h")
#         print(a, c)
#         print("a")
#         hanoi(n - 1, b, a, c)


# print(countt(n))
# hanoi(n, 1, 2, 3)

# 17478

# num = int(input())


# def solve(n, a):
#     str = ""
#     if n == 0:
#         print('_'*4*(n-a) + '"재귀함수가 뭔가요?"')
#         print('_'*4*(n-a) + '"재귀함수는 자기 자신을 호출하는 함수라네"')
#     else:
#         print('_'*4*(n-a) + '"재귀함수가 뭔가요?"')
#         print('_'*4*(n-a) + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#         print('_'*4*(n-a) + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
#         print('_'*4*(n-a) +
#               '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#         a -= 1
#         solve(n-1, a-1)
#         print('_'*4*(n-a) + "라고 답변하였지.")
#     return str


# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# print(solve(num, num), end="")
# print("라고 답변하였지.")

# 2447
num = int(input())


def star(n):
    star_list = []
    if n == 3:
        star_list = [["*", "*", "*"], ["*", " ", "*"], ["*", "*", "*"]]
    else:
        m = star(n//3)
        for i in range(3):
            for j in range(n//3):
                if i == 1:
                    star_list.append(m[j]+[' ']*(n//3)+m[j])
                    continue
                star_list.append(m[j]*3)
    return star_list


for i in star(num):
    for j in i:
        print(j, end="")
    print()
