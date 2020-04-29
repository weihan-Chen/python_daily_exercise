import calendar


def is_leap(year):
    is_leap = calendar.isleap(year)
    return is_leap


if __name__ == '__main__':
    year = int(input('何年：'))
    s = is_leap(year)
    print_leap_str = '%s年是闰年' if s else '%s年不是闰年\n'
    print(print_leap_str % year)
