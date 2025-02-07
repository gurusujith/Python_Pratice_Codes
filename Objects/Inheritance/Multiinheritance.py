class Demo1:
    def disp1(self):
        print("Iniside disp1")
class Demo2(Demo1):
    def disp2(self):
        print("Insisde disp2")
class Demo3(Demo2):
    pass
d3 = Demo3()
d3.disp1()
d3.disp2()