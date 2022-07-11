N = int(input())
people = []

for i in range(N):
    people.append([1, *map(int, input().split())])

for i in people:
    for j in people:
        if (i[1] < j[1]) & (i[2] < j[2]):
            i[0] += 1
    print(i[0], end=" ")