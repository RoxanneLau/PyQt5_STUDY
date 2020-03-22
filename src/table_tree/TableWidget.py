import sys
from PyQt5.QtWidgets import *

class TableWidget(QWidget):
    def __init__(self):
        super(TableWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget演示')
        self.resize(430,230)

        layout=QHBoxLayout()

        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])
        nameItem=QTableWidgetItem('小明')
        tableWidget.setItem(0,0,nameItem)

        ageItem=QTableWidgetItem('24')
        tableWidget.setItem(0,1,ageItem)

        jgItem=QTableWidgetItem('北京')
        tableWidget.setItem(0,2,jgItem)

        # 禁止编辑
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行显示
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 调整行和列
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()
        # 表格头的显示
        tableWidget.horizontalHeader().setVisible(False)
        tableWidget.setVerticalHeaderLabels(['A','B','C'])
        # 表格线
        tableWidget.setShowGrid(False)

        self.setLayout(layout)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=TableWidget()
    main.show()
    sys.exit(app.exec_())