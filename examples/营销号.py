# 输出营销号文章
def yingxiaohao(main_body, event, in_fact='没什么'):
    print('''{}{}是怎么回事呢？{}相信大家都很熟悉，但是{}{}是怎么回事呢，下面就让小编带大家一起了解吧。
{}{}，其实就是{}，大家可能会很惊讶{}怎么会{}呢？但事实就是这样，小编也感到非常惊讶。
这就是关于{}{}的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！'''.format(
        main_body,
        event,
        main_body,
        main_body,
        event,
        main_body,
        event,
        in_fact,
        main_body,
        event,
        main_body,
        event))


if __name__ == '__main__':
    main_body = str(input('主体：'))
    event = str(input('事件：'))
    in_fact = str(input('其实：'))
    yingxiaohao(main_body, event, in_fact)
