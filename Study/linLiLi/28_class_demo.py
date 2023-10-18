class students:
    def __init__(self, stu_name, stu_num):
        self.name = stu_name
        self.num = stu_num
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生{self.name}(学号:{self.num}) 的成绩为：")
        for course in self.grades:
            print(f"{course}: {self.grades[course]}分")


zhang = students("小张", "991103")
zhang.set_grade("数学", 90)
zhang.set_grade("语文", 99)
zhang.print_grades()
wang = students("小王", "990310")

print(zhang.name, zhang.grades, wang.name, wang.grades)
