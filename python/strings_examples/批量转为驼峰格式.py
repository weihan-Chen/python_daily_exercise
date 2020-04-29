import re


def camel(s):
    s = re.sub(r'(\s|_|-)+', ' ', s).title().replace(' ', '')
    return s


def batch_camel(slist):
    return [camel(s) for s in slist]


s = batch_camel(['student_id', 'student\tname', 'student-add'])
print(s)
