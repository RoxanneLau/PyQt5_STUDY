import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class FirstMainWindow(QMainWindow):
    def __init__(self):
        super(FirstMainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,250)

        # 设置主窗口的标题
        self.setWindowTitle('设置窗口图标')

        # 设置窗口的图标
        # self.setWindowIcon(QIcon('./images/Blinky.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 可以用于设置窗口和应用程序图标
    # app.setWindowIcon(QIcon('./images/Blinky.ico'))

    main = FirstMainWindow()
    main.show()
    sys.exit(app.exec_())