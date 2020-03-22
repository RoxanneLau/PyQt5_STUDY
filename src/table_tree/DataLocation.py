'''
在表格中快速定位到特定的行
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class DatdLocation(QWidget):
    def __init__(self):
        super(DatdLocation, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget例子')
        self.resize(600,800)

        layout=QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(40)
        tableWidget.setColumnCount(4)

        layout.addWidget(tableWidget)

        for i in range(40):
            for j in range(4):
                itemContent='(%d,%d)'%(i+1,j+1)
                tableWidget.setItem(i,j,QTableWidgetItem(itemContent))

        self.setLayout(layout)
        # 搜索满足条件的Cell
        text='(13,1)'
        items=tableWidget.findItems(text,Qt.MatchExactly)
        if len(items)>0:
            item=items[0]
            item.setBackground(QBrush(QColor(0,255,0)))
            item.setForeground(QBrush(QColor(255,0,0)))

            row=item.row()

            # 定位到指定行
            tableWidget.verticalScrollBar().setSliderPosition(row)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=DatdLocation()
    main.show()
    sys.exit(app.exec_())