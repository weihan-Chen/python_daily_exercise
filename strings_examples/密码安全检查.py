# 密码安全要求：6~20位，只包含英文字母和数字
import re


def password_check(password):
    pat = re.compile(r'[\da-zA-Z]{6,20}')
    return pat.fullmatch(password)


if __name__ == '__main__':
    password = input('password:')
    check_results = password_check(password)
    if check_results:
        print('password is illegal')
    else:
        print('password is OK')
