import time as t

class Mytimer():
    def __init__(self):
        self.says = '计时未开始！\n'
        self.unint = ['年', '月', '日', '小时', '分钟', '秒']
        self.getstart = []
        self.getstop = []

    def __str__(self):
        return self.says

   # __repr__ = __str__

    def start(self):
        self.getstart = []
        self.getstart = t.localtime()
        print('计时开始！\n')
        self.says = '请先调用stop。。。\n'
    def stop(self):
        self.getstop = []
        if self.getstart:
            self.getstop = t.localtime()
            self.calcu()
            print('计时结束!\n')
        else:
            print('请先调用start。。。\n')
    def calcu(self):
        self.delta = []
        self.says = '总共计时了: '
        for each in range(6):
            self.delta.append(self.getstop[each] - self.getstart[each])
            if self.delta[each]:
                self.says += str(self.delta[each]) + self.unint[each]

tt = Mytimer() #创建实例对象时执行__init__方法，其他过程不执行，不能放在循环内部，否者每次都需要创建实例对象执行init方法
while(1):
    words = input('输入‘start’开始计时，输入‘stop’停止计时，输入‘time’查询计时总时间,输入‘exit’退出\n')
    if words == 'start':
        tt.start()
    elif words == 'stop':
        tt.stop()
    elif words == 'time':
        print(tt)
    elif words == 'exit':
        break
    else:
        print('输入有误，请重新输入\n')
print('#运行结束，谢谢使用！#')



