class Student(object):
    def get__name(self):
        return self.__name
    
    def get__score(self):
        return self.__score
    
    def set__name(self, name):
        self.__name = name 
    
    def set__score(self, score):
        self.__score = score
    
    

student = Student()    #实例化可以只实例化一次，不同对象采用不同的实际参数，但是这样容易弄混，最好实例化为 lisi = Student() // zhangsan = Student()

student.set__name('zhangsan')
student.set__score(65)
print(student.get__name())
print(student.get__score())

student.set__name('lisi')
student.set__score(80)
print(student.get__name())
print(student.get__score())