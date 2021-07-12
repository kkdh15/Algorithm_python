n, k = map(int, input().split())
coins = []
count = 0

for _ in range(n):
  coins.append(int(input()))

coins.sort(reverse=True)

for coin in coins:
  if coin <= k:
    count += k//coin
    k %= coin
  
  if k==0:
    break

print(count)