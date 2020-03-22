'''
1. 关于；
2. 警告；
3. 错误；
4. 提问；
5. 消息。
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QmessageBoxDemo(QWidget):
    def __init__(self):
        super(QmessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBox案例')
        self.resize(300,400)

        layout=QVBoxLayout()
        self.button1=QPushButton()
        self.button1.setText('显示关于对话框')
        self.button1.clicked.connect(self.showDialog)

        self.button2=QPushButton()
        self.button2.setText('显示消息对话框')
        self.button2.clicked.connect(self.showDialog)

        self.button3 = QPushButton()
        self.button3.setText('显示警告对话框')
        self.button3.clicked.connect(self.showDialog)

        self.button4 = QPushButton()
        self.button4.setText('显示错误对话框')
        self.button4.clicked.connect(self.showDialog)

        self.button5 = QPushButton()
        self.button5.setText('显示提问对话框')
        self.button5.clicked.connect(self.showDialog)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)

        self.setLayout(layout)

    def showDialog(self):
        text=self.sender().text()
        if text=='显示关于对话框':
            QMessageBox.about(self,'关于','这是一个关于对话框')
        elif text=='显示消息对话框':
            QMessageBox.information(self,'消息','显示消息对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        elif text=='显示警告对话框':
            QMessageBox.warning(self,'警告','显示警告对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        elif text=='显示错误对话框':
            QMessageBox.critical(self,'错误','显示错误对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        elif text=='显示提问对话框':
            QMessageBox.question(self,'提问','显示提问对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=QmessageBoxDemo()
    main.show()
    sys.exit(app.exec_())
