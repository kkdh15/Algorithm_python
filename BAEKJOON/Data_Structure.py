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
class Deque():
    def __init__(self):
        self.deque = []

    def push_front(self, data):
        self.deque.insert(0, data)

    def push_rear(self, data):
        self.deque.append(data)

    def pop_front(self):
        if self.empty():
            return -1
        else:
            pop_item = self.deque[0]
            del self.deque[0]
            return pop_item

    def pop_rear(self):
        if self.empty():
            return -1
        else:
            pop_item = self.deque[-1]
            del self.deque[-1]
            return pop_item

    def size(self):
        return len(self.deque)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty():
            return -1
        else:
            return self.deque[0]

    def rear(self):
        if self.empty():
            return -1
        else:
            return self.deque[-1]


# 10866
import sys
N = int(sys.stdin.readline())
d = Deque()
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push_front':
        d.push_front(order[1])
    if order[0] == 'push_back':
        d.push_rear(order[1])
    if order[0] == 'pop_front':
        print(d.pop_front())
    if order[0] == 'pop_back':
        print(d.pop_rear())
    if order[0] == 'size':
        print(d.size())
    if order[0] == 'empty':
        print(d.empty())
    if order[0] == 'front':
        print(d.front())
    if order[0] == 'back':
        print(d.rear())
