class Student(object):
    def __init__(self, name, year, class_num, student_id):
        self.name = name
        self.year = year
        self.class_num = class_num
        self.student_id = student_id

    def introduce_id(self):
        return 'Name : {}, Grade {}, Class {}, {} th'.format(self.name, self.year, self.class_num, self.student_id)