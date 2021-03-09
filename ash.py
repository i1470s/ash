#PRIMARY IMPORTS

import PyQt5, sys, os, platform

#SECONDARY IMPORTS

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#UI IMPORTS

from data.ui.ui_splash_screen import Ui_SplashScreen
from data.ui.ui_main_screen import Ui_mainWindow
from data.ui.ui_chat_screen import Ui_chatWindow
from data.ui.ui_terminal_screen import Ui_terminalWindow

#SETTINGS

counter = 0



#MAIN WINDOW
class mainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(mainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QtGui.QIcon("./data/imgs/icon.png"))
        self.oldPos = self.pos()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        


#TERMINAL WINDOW
class terminalWindow(QWidget):
    def __init__(self):
        super(terminalWindow, self).__init__(*args, **kwargs)
        self.process = QProcess(self)
        self.terminal = QWidget(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.terminal)
        wid = str(int(self.terminal.winId()))
        self.process.start('urxvt', ['-embed', wid])

    def closeEvent(self, event):
        self.process.terminate()
        self.process.waitForFinished(1000)

        
        
#CHAT WINDOW
class chatWindow(QWidget):
    def __init__(self):
        super(chatWindow, self).__init__(*args, **kwargs)
 
 
 
# SPLASH SCREEN
class SplashScreen(QMainWindow):
    is_save = False
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./data/imgs/icon.png"))
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(60)

        self.ui.label_description.setText("<strong>Welcome to ash</strong>")

        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>Loading Database</strong>"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>Loading User Interface</strong>"))
		
        self.oldPos = self.pos()
        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = mainWindow()
            self.main.show()
            self.close()
        counter += 1    

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()



#LAUNCH APPLICATION
def launch():

		# First we created a application object for pyqt

		app = QApplication(sys.argv)

		# Next is we show the window then execute the app.

		window = SplashScreen()
		window.show()
		sys.exit(app.exec_())

if __name__ == '__main__':
    launch()
