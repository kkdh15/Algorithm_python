n = int(input())
cnt = 0

word_list = [input() for _ in range(n)]

for word in word_list:
    err = 0
    for index in range(len(word) - 1):
        if word[index] != word[index + 1]:
            new_word = word[index + 1 :]
            if new_word.count(word[index]) > 0:
                err += 1
    if err == 0:
        cnt += 1

print(cnt)
