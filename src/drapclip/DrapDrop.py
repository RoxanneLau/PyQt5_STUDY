import sys,math
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self,e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.addItem(e.mimeData().text())


class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        formLayout=QFormLayout()
        formLayout.addRow(QLabel('请将坐标的文本拖拽到右边的下拉列表中'))
        lineEdit=QLineEdit()
        lineEdit.setDragEnabled(True)

        combo=MyComboBox()
        formLayout.addRow(lineEdit,combo)
        self.setLayout(formLayout)
        self.setWindowTitle('拖拽案例')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=DrapDropDemo()
    main.show()
    sys.exit(app.exec_())