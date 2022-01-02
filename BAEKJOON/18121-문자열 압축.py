# 2020 카카오 신입 공채

def solution(s):
  if len(s) == 1:
    return 1
  
  result = 1000

  for i in range(1,len(s)//2 + 1):
    data = []
    data2 = []
    count = 1

    for j in range(0,len(s),i):
      data.append(s[j:j+i])

    for k in range(len(data)):
      if k != len(data)-1:
        if data[k] == data[k+1]:
          count += 1
        else:
          if count != 1: data2.append(str(count))
          data2.append(data[k])
          count = 1
      else:
        if count != 1: data2.append(str(count))
        data2.append(data[k])
  
    value = len(''.join(data2))

    result = min(result, value)

  return result


'''
간단한 알고리즘 
s = input()
result = []
count = 1

for i in range(len(s)):
  if i != len(s)-1:
    if s[i] == s[i+1]:
      count += 1
    else:
      if count != 1: result.append(str(count))
      result.append(s[i])
      count = 1
  else:
    if count != 1: result.append(str(count))
    result.append(s[i])

print(''.join(result))
'''