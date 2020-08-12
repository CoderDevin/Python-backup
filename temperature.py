class Centigrade():
    def __init__(self, value = 26.0):
        self.grade = float(value)

    def __get__(self, instance, owner):
        return self.grade

    def __set__(self, instance, value):
        self.grade = float(value)

class Fahrenheit():
    def __get__(self, instance, owner):
        return (instance.cen * 1.8) + 32

    def __set__(self, instance, value):
        instance.cen = (float(value) - 32) / 1.8

class Mytemperature():
    fah = Fahrenheit()
    cen = Centigrade()

temp = Mytemperature()
while (1):
    command = input("输入'cen'转换为摄氏度，输入'fah'转换为华氏度,输入'exit'退出\n")
    if command == 'cen':
        data = eval(input("输入要转换的数据：fahrenheit = "))
        temp.fah = data
        print("centigrade =", temp.cen)
    elif command == 'fah':
        data = eval(input("输入要转换的数据：centigrade = "))
        temp.cen = data
        print("fahrenheit = ", temp.fah)
    elif command == "exit":
        break
    else:
        print("输入命令有误，请重新输入！！！\n")
print("完成！谢谢使用！\n")