import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout=QVBoxLayout()

        self.button1=QPushButton('first button')
        self.button1.setText('button1')
        self.button1.setCheckable(True)
        self.button1.toggle()
        # self.button1.clicked.connect(self.whichButton)
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))

        layout.addWidget(self.button1)
        self.setLayout(layout)

    # 使用lambda表达式连接信号和槽
    '''def whichButton(self,btn):
        print('被单击的按钮是<'+btn.text()+'>')'''

    def whichButton(self, btn):
        print('被单击的按钮是<' + btn.text() + '>')


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())