class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color
    def speak(self):
        print("喵" * self.age)
    def think(self,content):
        print(f"小猫{self.name}在思考{content}...")

cat1 = CuteCat("Jojo",2,"橘色")
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")
cat1.think("现在去抓沙发还是去抓纸箱")
