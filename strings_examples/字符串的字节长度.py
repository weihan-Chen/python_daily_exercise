def str_byte_len(mystr):
    return (len(mystr.encode('utf-8')))


# example
print(str_byte_len('i love python'))
print(str_byte_len('字符'))
