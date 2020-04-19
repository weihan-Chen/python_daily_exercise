# 逢7游戏自动输出
i = 1
while i <= 100:
    if i % 7 == 0:
        i += 1
        continue
    elif i % 10 == 7:
        i += 1
        continue
    elif i // 10 == 7:
        i += 1
        continue
    else:
        print(i)
    i += 1
