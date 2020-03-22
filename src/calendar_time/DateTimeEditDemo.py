import sys,math
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        layout=QVBoxLayout()
        dateTimeEdit1=QDateTimeEdit()
        dateTimeEdit2=QDateTimeEdit()
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))
        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)

        self.dateTimeEdit=dateTimeEdit1

        dateTimeEdit2.setCalendarPopup(True)

        dateEdit=QDateTimeEdit(QDate.currentDate())
        timeEdit=QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        dateTimeEdit2.setDisplayFormat('yyyy/MM/dd HH-mm-ss')

        dateEdit.setDisplayFormat('yyyy.MM.dd')
        timeEdit.setDisplayFormat('HH:mm:ss')

        layout.addWidget(dateTimeEdit1)
        layout.addWidget(dateTimeEdit2)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)

        self.btn=QPushButton('获取日期和时间')
        self.btn.clicked.connect(self.onButtonClick)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        self.resize(300,90)
        self.setWindowTitle('设置不同风格的日期和时间')

    # 日期变换
    def onDateChanged(self,date):
        print(date)

    # 时间变化
    def onTimeChanged(self,time):
        print(time)

    # 日期时间变化
    def onDateTimeChanged(self,datetime):
        print(datetime)

    # 按钮按下
    def onButtonClick(self):
        dateTime=self.dateTimeEdit.dateTime()
        print(dateTime)

        # 最大日期
        print(self.dateTimeEdit.maximumDate())

        # 最大日期和时间
        print(self.dateTimeEdit.maximumDateTime())


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=DateTimeEditDemo()
    main.show()
    sys.exit(app.exec_())