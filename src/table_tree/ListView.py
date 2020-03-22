'''
显示列表数据
'''
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class TableView(QWidget):

    def __init__(self,parent=None):
        super(TableView, self).__init__(parent)
        self.setWindowTitle('QListView例子')
        self.resize(300,270)

        layout=QVBoxLayout()

        listView=QListView()
        listModel=QStringListModel()
        self.list=['列表项1','列表项2','列表项3']

        listModel.setStringList(self.list)

        listView.setModel(listModel)
        listView.clicked.connect(self.clicked)

        layout.addWidget(listView)
        self.setLayout(layout)

    def clicked(self,item):
        QMessageBox.information(self,'QListView','您选择了:'+self.list[item.row()])


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=TableView()
    main.show()
    sys.exit(app.exec_())