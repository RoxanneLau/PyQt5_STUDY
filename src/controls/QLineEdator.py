'''
限制只能输入整数、浮点数或者满足一定条件的字符串
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        # 创建表单布局
        formLayout=QFormLayout()

        intLineEdit=QLineEdit()
        doubleLineEdit=QLineEdit()
        validatorLineEdit=QLineEdit()

        formLayout.addRow('整数类型',intLineEdit)
        formLayout.addRow('浮点数类型',doubleLineEdit)
        formLayout.addRow('数字和字母类型',validatorLineEdit)

        intLineEdit.setPlaceholderText('整型')
        doubleLineEdit.setPlaceholderText('浮点型')
        validatorLineEdit.setPlaceholderText('数字和字母')

        # 整数校验器
        intValidator=QIntValidator(self)
        intValidator.setRange(1,99)

        # 浮点校验器
        doubleValidator=QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        # 正常显示
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度
        doubleValidator.setDecimals(2)

        # 字符和数字
        reg=QRegExp('[a-zA-Z0-9]+$')
        validator=QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=QLineEditValidator()
    main.show()
    sys.exit(app.exec_())