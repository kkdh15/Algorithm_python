a = input()
cnt = len(a)

cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro_list:
    if i in a:
        cnt -= a.count(i)

print(cnt)
