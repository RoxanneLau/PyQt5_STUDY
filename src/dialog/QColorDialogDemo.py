import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Dialog例子')
        layout=QVBoxLayout()
        self.colorButton=QPushButton('选择颜色')
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)

        self.colorButton1 = QPushButton('选择背景色')
        self.colorButton1.clicked.connect(self.getBGColor)
        layout.addWidget(self.colorButton1)

        self.colorLabel = QLabel('Hello 测试颜色')
        self.colorLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)

    def getColor(self):
        color = QColorDialog.getColor()
        p=QPalette()
        p.setColor(QPalette.WindowText,color)
        self.colorLabel.setPalette(p)

    def getBGColor(self):
        color = QColorDialog.getColor()
        p=QPalette()
        p.setColor(QPalette.Window,color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)


if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = QColorDialogDemo()
        main.show()
        sys.exit(app.exec_())