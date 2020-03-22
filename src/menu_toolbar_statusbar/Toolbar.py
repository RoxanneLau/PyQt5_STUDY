'''
工具栏默认只显示图标，悬停显示提示
'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Toolbar(QMainWindow):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('工具栏例子')
        self.resize(300,200)
        tb1=self.addToolBar('File')
        new=QAction(QIcon('D:\JetBrains\PyCharmProjects\pyqt10\src\controls\images\Carrot Bonus.ico'),'new',self)
        tb1.addAction(new)

        open=QAction(QIcon('D:\JetBrains\PyCharmProjects\pyqt10\src\controls\images\Cherry Bonus.ico'),'open',self)
        tb1.addAction(open)

        save=QAction(QIcon('D:\JetBrains\PyCharmProjects\pyqt10\src\controls\images\Dig Dug.ico'),'save',self)
        tb1.addAction(save)

        tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb2=self.addToolBar('File1')
        new1=QAction(QIcon('D:\JetBrains\PyCharmProjects\pyqt10\src\controls\images\Eggplant Bonus.ico'),'新建',self)
        tb2.addAction(new1)
        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb1.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self,a):
        print('按下的工具栏是',a.text())


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=Toolbar()
    main.show()
    sys.exit(app.exec_())