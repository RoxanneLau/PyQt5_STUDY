'''
支持MVC和非MVC模式
'''
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class TableView(QMainWindow):

    def __init__(self,parent=None):
        super(TableView, self).__init__(parent)
        self.setWindowTitle('QListWidget例子')
        self.resize(300,270)

        self.listWidget=QListWidget()
        self.listWidget.resize(300,120)
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')
        self.listWidget.addItem('item4')
        self.listWidget.addItem('item5')

        self.listWidget.itemClicked.connect(self.clicked)

        # 直接充满整个屏幕
        self.setCentralWidget(self.listWidget)

    def clicked(self,Index):
        QMessageBox.information(self,'QListWidget','您选择了：'+self.listWidget.item(self.listWidget.row(Index)).text())


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=TableView()
    main.show()
    sys.exit(app.exec_())