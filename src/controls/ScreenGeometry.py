import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget
def onClick_Button():
    # 不包含边框
    print('1')
    print('widget.x()=%d'%widget.x())# 窗口横坐标
    print('widget.y()=%d' % widget.y())# 窗口纵坐标
    print('widget.width()=%d' % widget.width())# 工作区宽度
    print('widget.height()=%d' % widget.height())# 工作区高度

    # 使用触发器，含有边框
    print('2')
    print('widget.geometry().x()=%d'% widget.geometry().x())# 工作区横坐标
    print('widget.geometry().y()=%d' % widget.geometry().y())# 工作区纵坐标
    print('widget.geometry().width()=%d' % widget.geometry().width())# 工作区宽度
    print('widget.geometry().height()=%d' % widget.geometry().height())# 工作区高度

    # 含有标题栏
    print('3')
    print('widget.frameGeometry().x()=%d'%widget.frameGeometry().x())# 窗口横坐标
    print('widget.frameGeometry().y()=%d' % widget.frameGeometry().y())# 窗口纵坐标
    print('widget.frameGeometry().width()=%d' % widget.frameGeometry().width())# 窗口宽度
    print('widget.frameGeometry().height()=%d' % widget.frameGeometry().height())# 窗口高度

app=QApplication(sys.argv)

# 创建窗口
widget=QWidget()
btn=QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick_Button)
btn.move(24,52)

# 设置工作区的尺寸
widget.resize(300,240)
widget.move(250,200)

widget.setWindowTitle('屏幕坐标系')
widget.show()
sys.exit(app.exec_())