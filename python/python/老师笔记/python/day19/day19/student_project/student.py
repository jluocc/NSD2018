

# 实现Student类
class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s

    def get_infos_string(self):
        return (self.name,
                str(self.age),
                str(self.score))
    
    def get_name(self):
        return self.name
    
    def get_score(self):
        return self.score

    def get_age(self):
        return self.age

    def write_to_file(self, file):
        file.write(self.name)
        file.write(',')
        file.write(str(self.age))
        file.write(',')
        file.write(str(self.score))
        file.write('\n')
