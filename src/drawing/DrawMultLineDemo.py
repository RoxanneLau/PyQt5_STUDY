import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DrawMultLineDemo(QWidget):
    def __init__(self):
        super(DrawMultLineDemo, self).__init__()
        self.resize(300,300)
        self.setWindowTitle('绘制Pen的样式')

    def paintEvent(self,event):
        painter=QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)

        # 创建画笔
        pen=QPen(Qt.red,Qt.SolidLine)

        # 第一条
        painter.setPen(pen)
        painter.drawLine(20,40,250,40)

        # 第二条
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20,80,250,80)

        # 第三条
        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20,120,250,120)

        # 第四条
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20,160,250,160)

        # 第五条
        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        # 自定义
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,4,5,4])
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        # 显示
        size=self.size()
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultLineDemo()
    main.show()
    sys.exit(app.exec_())
