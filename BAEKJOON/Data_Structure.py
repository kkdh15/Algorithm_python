# 10828
# import sys
# N = int(sys.stdin.readline())
# lst = []
# for i in range(N):
#     order = sys.stdin.readline().split()
#     if order[0] == "push":
#         lst.append(int(order[1]))
#     if order[0] == "pop":
#         if(len(lst) == 0):
#             print(-1)
#         else:
#             a = lst[-1]
#             del lst[-1]
#             print(a)
#     if order[0] == "size":
#         print(len(lst))
#     if order[0] == "empty":
#         if(len(lst) == 0):
#             print(1)
#         else:
#             print(0)
#     if order[0] == "top":
#         if(len(lst) == 0):
#             print(-1)
#         else:
#             print(lst[-1])

# 9093
# import sys
# N = int(sys.stdin.readline())
# for i in range(N):
#     sent = input().split()
#     for j in range(len(sent)):
#         sent[j] = sent[j][::-1]
#         print(sent[j], end=" ")
#     print()

# 9012
# import sys
# N = int(input())
# for i in range(N):
#     vps = input()
#     cnt = 0
#     for j in range(len(vps)):
#         if vps[j] == '(':
#             cnt += 1
#         else:
#             cnt -= 1
#         if cnt < 0:
#             break
#     if cnt == 0:
#         print("YES")
#     else:
#         print("NO")

# STACK
# class Stack():
#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if self.empty():
#             return -1
#         else:
#             pop_item = self.stack[-1]
#             del self.stack[-1]
#             return pop_item

#     def size(self):
#         return len(self.stack)

#     def empty(self):
#         if self.size() == 0:
#             return 1
#         else:
#             return 0

#     def top(self):
#         if self.empty():
#             return -1
#         else:
#             return self.stack[-1]


# N = int(input())
# s = Stack()
# for i in range(N):
#     order = input().split()
#     if order[0] == 'push':
#         s.push(order[1])
#     if order[0] == 'pop':
#         print(s.pop())
#     if order[0] == 'size':
#         print(s.size())
#     if order[0] == 'empty':
#         print(s.empty())
#     if order[0] == 'top':
#         print(s.top())

# QUEUE
# class Queue():
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, data):
#         self.queue.append(data)

#     def dequeue(self):
#         if self.empty():
#             return -1
#         else:
#             dequeue_item = self.queue[0]
#             del self.queue[0]
#             return dequeue_item

#     def size(self):
#         return len(self.queue)

#     def empty(self):
#         if self.size() == 0:
#             return 1
#         else:
#             return 0

#     def front(self):
#         if self.empty():
#             return -1
#         else:
#             return self.queue[0]

#     def rear(self):
#         if self.empty():
#             return -1
#         else:
#             return self.queue[-1]


# # 10845
# N = int(input())
# q = Queue()
# for i in range(N):
#     order = input().split()
#     if order[0] == 'push':
#         q.enqueue(order[1])
#     if order[0] == 'pop':
#         print(q.dequeue())
#     if order[0] == 'size':
#         print(q.size())
#     if order[0] == 'empty':
#         print(q.empty())
#     if order[0] == 'front':
#         print(q.front())
#     if order[0] == 'back':
#         print(q.rear())

# DEQUE
# class Deque():
#     def __init__(self):
#         self.deque = []

#     def push_front(self, data):
#         self.deque.insert(0, data)

#     def push_rear(self, data):
#         self.deque.append(data)

#     def pop_front(self):
#         if self.empty():
#             return -1
#         else:
#             pop_item = self.deque[0]
#             del self.deque[0]
#             return pop_item

#     def pop_rear(self):
#         if self.empty():
#             return -1
#         else:
#             pop_item = self.deque[-1]
#             del self.deque[-1]
#             return pop_item

#     def size(self):
#         return len(self.deque)

#     def empty(self):
#         if self.size() == 0:
#             return 1
#         else:
#             return 0

#     def front(self):
#         if self.empty():
#             return -1
#         else:
#             return self.deque[0]

#     def rear(self):
#         if self.empty():
#             return -1
#         else:
#             return self.deque[-1]


# # 10866
# import sys
# N = int(sys.stdin.readline())
# d = Deque()
# for i in range(N):
#     order = sys.stdin.readline().split()
#     if order[0] == 'push_front':
#         d.push_front(order[1])
#     if order[0] == 'push_back':
#         d.push_rear(order[1])
#     if order[0] == 'pop_front':
#         print(d.pop_front())
#     if order[0] == 'pop_back':
#         print(d.pop_rear())
#     if order[0] == 'size':
#         print(d.size())
#     if order[0] == 'empty':
#         print(d.empty())
#     if order[0] == 'front':
#         print(d.front())
#     if order[0] == 'back':
#         print(d.rear())

# 1874
# import sys


# class Stack():
#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if self.empty():
#             return -1
#         else:
#             pop_item = self.stack[-1]
#             del self.stack[-1]
#             return pop_item

#     def size(self):
#         return len(self.stack)

#     def empty(self):
#         if self.size() == 0:
#             return 1
#         else:
#             return 0

#     def top(self):
#         if self.empty():
#             return -1
#         else:
#             return self.stack[-1]


# n = int(sys.stdin.readline())
# lst = []
# for i in range(n):
#     lst.append(int(sys.stdin.readline()))

# q = Stack()
# cur = 1
# i = 0
# ans_lst = []
# pop_item = 0
# for _ in range(n*2):
#     if q.top() == lst[i]:
#         pop_item = q.pop()
#         ans_lst.append("-")
#         i += 1
#     else:
#         q.push(cur)
#         ans_lst.append("+")
#         cur += 1


# if pop_item == lst[-1]:
#     for i in ans_lst:
#         print(i)
# else:
#     print("NO")

# 1406 시간복잡도 중요 !! 스택의 pop, append O(1) 임
#                           insert del 등은 O(N)이다
# import sys

# sent = list(sys.stdin.readline().strip())
# sent2 = []

# n = int(sys.stdin.readline())
# for i in range(n):
#     order = sys.stdin.readline().split()
#     if order[0] == 'L':
#         if sent:
#             sent2.append(sent.pop())
#     if order[0] == 'D':
#         if sent2:
#             sent.append(sent2.pop())
#     if order[0] == 'B':
#         if sent:
#             sent.pop()
#     if order[0] == 'P':
#         sent.append(order[1])

# print("".join(sent+list(reversed(sent2))))

# 1158
# n, k = map(int, input().split())
# p_lst = [i for i in range(1, n+1)]
# a_lst = []
# num = 0
# for i in range(n):
#     num += k-1
#     if num >= len(p_lst):
#         num = num % len(p_lst)
#     a_lst.append(str(p_lst.pop(num)))

# print("<", ", ".join(a_lst), ">", sep="")

# 17413
# s = list(input())
# tag = False
# word = ''
# result = ''
# for i in s:
#     if tag == False:
#         if i == '<':
#             tag = True
#             word = word+i
#         elif i == ' ':
#             word = word+i
#             result = result+word
#             word = ''
#         else:
#             word = i+word

#     elif tag == True:
#         word = word+i
#         if i == '>':
#             tag = False
#             result = result+word
#             word = ''

# print(result+word)

# 10799
# razor = list(input())
# answer = 0
# st = []

# for i in range(len(razor)):
#     if razor[i] == '(':
#         st.append('(')

#     else:
#         if razor[i-1] == '(':
#             st.pop()
#             answer += len(st)

#         else:
#             st.pop()
#             answer += 1

# print(answer)


# 17298
# import sys
# N = int(sys.stdin.readline().rstrip())
# seq = list(map(int, sys.stdin.readline().rstrip().split()))
# stack = []

# for i in range(N):
#     while stack:
#         if seq[i] > seq[stack[-1]]:
#             seq[stack.pop()] = seq[i]
#         else:
#             stack.append(i)
#             break
#     if not stack:
#         stack.append(i)

# for i in stack:
#     seq[i] = -1

# print(*seq)

# 17299
# from collections import Counter
# import sys
# N = int(sys.stdin.readline())
# seq = list(map(int, sys.stdin.readline().split()))
# stack = []
# dic = Counter(seq) ## Counter로 dict를 만들어 시간 줄이기
# # dic = {}

# # for i in seq:
# #     dic[i] = seq.count(i)

# result = [-1] * N
# for i in range(N):
#     while stack:
#         if dic[seq[i]] > dic[seq[stack[-1]]]:
#             result[stack.pop()] = seq[i]
#         else:
#             stack.append(i)
#             break
#     if not stack:
#         stack.append(i)

# print(*result)

# 11655
# lower_alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# upper_alpha_list = [i.upper() for i in lower_alpha_list]

# s = list(input())
# for i in range(len(s)):
#     if s[i] in lower_alpha_list:
#         s[i] = lower_alpha_list[(lower_alpha_list.index(s[i])+13) % 26]
#     elif s[i] in upper_alpha_list:
#         s[i] = upper_alpha_list[(upper_alpha_list.index(s[i])+13) % 26]

# print(''.join(s))

# 11656
# s = list(input())
# dic = []

# for i in range(len(s)):
#     dic.append(s[i:])
# dic.sort()
# for i in dic:
#     print(''.join(i))

# 1935

# N = int(input())
# s = list(input())
# stack = []
# dic = {}
# alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
#          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# for i in alpha:
#     dic[i] = 0
# for i in range(N):
#     dic[alpha[i]] = int(input())

# for i in s:
#     if i.isalpha():
#         stack.append(dic[i])
#     else:
#         if i == '*':
#             stack[-2] = stack[-2] * stack[-1]
#         elif i == '/':
#             stack[-2] = stack[-2] / stack[-1]
#         elif i == '+':
#             stack[-2] = stack[-2] + stack[-1]
#         elif i == '-':
#             stack[-2] = stack[-2] - stack[-1]
#         stack.pop()

# print("{:.2f}".format(stack[0]))

# 1918
s = list(input())
stack = []
answer = ''

for i in s:
    if i.isalpha():
        answer += i
    else:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(i)

while stack:
    answer += stack.pop()

print(answer)
