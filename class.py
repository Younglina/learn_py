class Studen:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def play(self):
        print(f'学生{self.name}正在玩游戏')

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')

    def __repr__(self):
        return f'{self.name}:{self.age}'

studen1 = Studen('哈哈', 23)
studen1.play()
studen1.study('化学')
print(studen1)