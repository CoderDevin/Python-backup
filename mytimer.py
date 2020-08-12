import time as t

class Mytimer():
    def __init__(self):
        self.uint = ("年","月","日","小时","分钟","秒")
        self.says = "计时未开始"
        self.getstart = []
        self.getstop  = []
        self.delta = []

    def __str__(self):
        return self.says
    __repr__ = __str__


    def start(self):
        self.getstart = t.localtime()
        self.says = "请先调用stop。。。"
        print("计时开始！")

    def stop(self):
        if self.getstart:
            self.getstop = t.localtime()
            print("计时结束！")
            self.calcu()
        else:
            print("请先调用start。。。")

    def calcu(self):
        self.delta = []
        self.says = "总共进行了"
        for each in range(6):
            self.delta.append(self.getstop[each] - self.getstart[each])
            if self.delta[each]:
                self.says += str(self.delta[each]) + self.uint[each]
        self.getstart = []
        self.getstop  = []

tt = Mytimer()
while(1):
    print("###输入‘time’查询计时总时间，输入‘start’开始计时，输入‘stop’停止计时，确认回车即可###")
    command = input("请输入口令：")

    if command == 'time':
        print(tt)

    elif command == 'start':
        tt.start()
    elif command == 'stop':
        tt.stop()
    else:
        print("输入有误，请重新输入！")