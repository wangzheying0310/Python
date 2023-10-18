# 类继承练习：人力系统
# 员工分类：全职员工 FullTimeEmployee 和兼职员工 PartTimeEmployee
# 全职和兼职都有姓名 name 和工号 id
# 都具备打印信息 print_info 姓名和工号的方法
# 全职有月薪 monthly_salary
# 兼职有日新 daily_salary 每天月工作数的属性 work_days
# 全职和兼职都有计算月薪 calculate_monthly_pay 的方法 但计算过程不一样

class Employee:
    def __init__(self, hum_name, hum_id):
        self.name = hum_name
        self.id = hum_id

    def print_info(self):
        print(f"{self.name}的工号为{self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, hum_name, hum_id, monthly_salary):
        super().__init__(hum_name, hum_id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, hum_name, hum_id, daily_salary, work_days):
        super().__init__(hum_name, hum_id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days


zhang = FullTimeEmployee("张", "991103", 9000)
wang = PartTimeEmployee("王", "990310", 200, 15)
zhang.print_info()
wang.print_info()
print(zhang.calculate_monthly_pay())
print(wang.calculate_monthly_pay())