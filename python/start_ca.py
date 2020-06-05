import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculator import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        # 定义全局变量
        self.str1 = ''     # 第一个数
        self.str2 = ''     # 第二个数
        self.flag = '0'    # 正在输入第几个数标志
        self.calFlag = ''  # 运算标志
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 数字键事件处理
        self.ui.pushButton_10.clicked.connect(self.func_button3)  # 按钮3
        self.ui.pushButton_3.clicked.connect(self.func_button4)  # 按钮4
        self.ui.pushButton_4.clicked.connect(self.func_button1)  # 按钮1
        self.ui.pushButton_7.clicked.connect(self.func_button2)  # 按钮2
        self.ui.pushButton_9.clicked.connect(self.func_button6)  # 按钮6
        self.ui.pushButton_6.clicked.connect(self.func_button5)  # 按钮5
        self.ui.pushButton.clicked.connect(self.func_button7)  # 按钮7
        self.ui.pushButton_2.clicked.connect(self.func_button8)  # 按钮8
        self.ui.pushButton_8.clicked.connect(self.func_button9)  # 按钮9
        self.ui.pushButton_11.clicked.connect(self.func_button0)  # 按钮0

        # 符号键事件处理
        self.ui.pushButton_13.clicked.connect(self.func_buttonCE)  # 按钮CE
        self.ui.pushButton_14.clicked.connect(self.func_buttonMul)  # 按钮*
        self.ui.pushButton_15.clicked.connect(self.func_buttonDiv)  # 按钮/
        self.ui.pushButton_5.clicked.connect(self.func_buttonAdd)  # 按钮+
        self.ui.pushButton_12.clicked.connect(self.func_buttonDec)  # 按钮-
        self.ui.pushButton_16.clicked.connect(self.func_buttonEqual)  # 按钮=

    # 数字按钮函数
    def func_button1(self):
        if self.flag == '1':
            self.str2 = self.str2 + '1'     # self.str2 + "1" 的原因是为了输入多位数，多位数在输入法的时候都是字符串，故而没输入一位就是一位数，
                                            # 不存在个十百千的换算。 （感觉用insert函数更好一点，不需要）
            self.ui.lineEdit.setText(self.str2)     #setText的作用是像LineEdit 窗口输送文本
        else:
            self.str1 = self.str1 + '1'
            self.ui.lineEdit.setText(self.str1)

    def func_button2(self):
        if self.flag == '1':
            self.str2 = self.str2 + '2'

            self.ui.lineEdit.setText(self.str2)
        else:
            self.str1 = self.str1 + '2'
            self.ui.lineEdit.setText(self.str1)

    def func_button3(self):
        if self.flag == '1':
            self.str2 = self.str2 + '3'

            self.ui.lineEdit.setText(self.str2)
        else:
            self.str1 = self.str1 + '3'
            self.ui.lineEdit.setText(self.str1)

    def func_button4(self):
        if self.flag == '1':
            self.str2 = self.str2 + '4'

            self.ui.lineEdit.setText(self.str2)
        else:
            self.str1 = self.str1 + '4'
            self.ui.lineEdit.setText(self.str1)

    def func_button5(self):
        if self.flag == '1':
            self.str2 = self.str2 + '5'

            self.ui.lineEdit.setText(self.str2)
        else:
            self.str1 = self.str1 + '5'
            self.ui.lineEdit.setText(self.str1)

    def func_button6(self):
        if self.flag == '1':
            self.str2 = self.str2 + '6'

            self.ui.lineEdit.setText(self.str2)
        else:
            self.str1 = self.str1 + '6'
            self.ui.lineEdit.setText(self.str1)

    def func_button7(self):
        if self.flag == '1':
            self.str2 = self.str2 + '7'

            self.ui.lineEdit.setText(self.str2)
        else:
            self.str1 = self.str1 + '7'
            self.ui.lineEdit.setText(self.str1)

    def func_button8(self):
        if self.flag == '1':
            self.str2 = self.str2 + '8'

            self.ui.lineEdit.setText(self.str2)
        else:
            self.str1 = self.str1 + '8'
            self.ui.lineEdit.setText(self.str1)

    def func_button9(self):
        if self.flag == '1':
            self.str2 = self.str2 + '9'

            self.ui.lineEdit.setText(self.str2)
        else:
            self.str1 = self.str1 + '9'
            self.ui.lineEdit.setText(self.str1)

    def func_button0(self):
        if self.flag == '1':
            self.str2 = self.str2 + '0'

            self.ui.lineEdit.setText(self.str2)
        else:
            self.str1 = self.str1 + '0'
            self.ui.lineEdit.setText(self.str1)

    # 运算按钮函数
    def func_buttonAdd(self):
        self.ui.lineEdit.setText(self.str2)
        self.flag = '1'
        self.calFlag = '1'

    def func_buttonDec(self):
        self.ui.lineEdit.setText(self.str2)
        self.flag = '1'
        self.calFlag = '2'

    def func_buttonMul(self):
        self.ui.lineEdit.setText(self.str2)
        self.flag = '1'
        self.calFlag = '3'

    def func_buttonDiv(self):
        self.ui.lineEdit.setText(self.str2)
        self.flag = '1'
        self.calFlag = '4'

    def func_buttonCE(self):
        """if self.flag == '0':
            self.str1 = ''
        else:
            self.str2 = ''               这里只是改变了str2的参数并没有改变str1的参数  因此ce只能清楚一个参数
        self.ui.lineEdit.setText('')      这里只是像窗口输入空格，但是并没有改变str1和str2的参数，因此如果没有改变上面的代码，参数的输入会有问题"""
        
        self.ui.lineEdit.clear() 
        self.str1 = '' 
        self.str2 = '' 
        self.flag = '0'                  #这样ce就实现了清楚所有缓存，重新输入str1和str2的参数

    def func_buttonEqual(self):
        global num
        # 字符串先转换为数字，计算结果后再转换为字符串
        if self.calFlag == '1':
            num = str(int(self.str1) + int(self.str2))     #由于输入的都是字符串，故而在进行数值运算的时候需要转化成int类型，输出时在转化为
        elif self.calFlag == '2':                          #str类型，方便setText的传递
            num = str(int(self.str1) - int(self.str2))
        elif self.calFlag == '3':
            num = str(int(self.str1) * int(self.str2))
        elif self.calFlag == '4':
            num = str(int(self.str1) / int(self.str2))
        self.ui.lineEdit.setText(num)
        self.str1 = ''
        self.str2 = ''
        self.flag = '0'
        self.calFlag = ''


# 主函数
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())