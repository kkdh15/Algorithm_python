# 2525
# hour, minute = map(int, input().split())
# time = int(input())
# hour += (minute + time)//60
# if(hour >= 24):
#     hour %= 24
# minute = (minute + time) % 60
# print(hour, minute)

# 2480
# f_dice, s_dice, t_dice = map(int, input().split())
# reward = 0
# dice_list = [f_dice, s_dice, t_dice]
# reward_list = [0, 0, 0, 0, 0, 0, 0]
# for i in dice_list:
#     reward_list[i] += 1
# count = max(reward_list)
# if count == 3:
#     reward = 10000 + reward_list.index(count) * 1000
# elif count == 2:
#     reward = 1000 + reward_list.index(count) * 100
# else:
#     reward = max(dice_list) * 100
# print(reward)
