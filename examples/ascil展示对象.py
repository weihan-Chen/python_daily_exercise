class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'id = ' + self.id + ', name =' + self.name


小明 = Student(id='001', name='小明')
print(小明)
