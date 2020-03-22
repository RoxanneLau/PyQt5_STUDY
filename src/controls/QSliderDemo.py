import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块控件演示')
        self.resize(300,700)

        layout=QVBoxLayout()
        self.label=QLabel('你好')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.slider=QSlider(Qt.Horizontal)
        # 设置最大值
        self.slider.setMaximum(48)
        # 设置最小值
        self.slider.setMinimum(12)
        # 步长
        self.slider.setSingleStep(3)
        # 设置当前值
        self.slider.setValue(18)
        # 设置刻度的位置
        self.slider.setTickPosition(QSlider.TicksBelow)
        # 设置刻度间的间隔
        self.slider.setTickInterval(6)

        self.slider1=QSlider(Qt.Vertical)
        # 设置最大值
        self.slider1.setMaximum(60)
        # 设置最小值
        self.slider1.setMinimum(10)
        # 步长
        self.slider1.setSingleStep(5)
        # 设置当前值
        self.slider1.setValue(30)
        # 设置刻度的位置
        self.slider1.setTickPosition(QSlider.TicksLeft)
        # 设置刻度间的间隔
        self.slider1.setTickInterval(2)

        layout.addWidget(self.slider)
        layout.addWidget(self.slider1)

        self.slider.valueChanged.connect(self.valueChanged)
        self.slider1.valueChanged.connect(self.valueChanged)
        self.setLayout(layout)

    def valueChanged(self):
        print('当前值：%s'%self.slider.value())
        # size=self.slider.value()
        size = self.sender().value()
        self.label.setFont(QFont('Arial',size))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=QSliderDemo()
    main.show()
    sys.exit(app.exec_())