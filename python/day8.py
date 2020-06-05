class other():
    def override(self):
        print("other override()")

    def implicit(self):
        print("other implicit()")
    
    def altered(self):
        print("other altered()")

class child():
    def __init__(self):
        self.a = other()
    
    def implicit(self):
        self.a.implicit()
    
    def override(self):
        print("child override()")
    
    def altered(self):
        print("child altered()")
        self.a.altered()
        print("child!")
    
son = child()

son.implicit()
son.override()
son.altered()

print("--------------------")

class Desc:
    def __get__(self, ins, cls):
        print('self in Desc: %s ' % self )
        print(self, ins, cls)
class Test:
    x = Desc()
    def prt(self):
        print('self in Test: %s' % self)
t = Test()
t.prt()
t.x