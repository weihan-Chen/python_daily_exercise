# 引入随机数生成模块
import random

# 设置人物数量和队伍数量
while True:
    people_summary = int(input('人物数量：'))
    group_summary = int(input('队伍数量：'))
    a = people_summary % group_summary
    if a != 0:
        print('不能平均分配，请重新输入')
    else:
        break

# 生成人物编号与所在队伍的字典
people_number = [1]
cnt = 2
while cnt <= people_summary:
    people_number.append(cnt)
    cnt += 1
people_group = dict.fromkeys(people_number, 0)

# 随机将所有人放入不同的队伍
cnt = 1
summary = [
    0,
]
i = 2
while i <= group_summary:
    summary.append(0)
    i += 1
while cnt <= people_summary:
    people_group[cnt] = num = random.randint(1, group_summary)
    summary[num - 1] += 1
    if summary[num - 1] >= people_summary / group_summary + 1:
        summary[num - 1] -= 1
        continue
    cnt += 1
# 输出结果
print('每组人数', summary[0])
i = 1
while i <= group_summary:
    print('第{}组:'.format(i))
    for group in people_group.values():
        if group == i:
            print(list(people_group.keys())[list(
                people_group.values()).index(group)],
                  end=', ')
            people_group[list(people_group.keys())[list(
                people_group.values()).index(group)]] = 0
    print('\n')
    i += 1
