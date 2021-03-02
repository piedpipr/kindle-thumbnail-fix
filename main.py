import sys
import pyudev
from threading import Thread
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QLabel, QWidget, QFileDialog, QLineEdit, QProgressBar
from PyQt5.QtGui import QMovie
from package.find_and_rename import find_and_rename


def app():

        def kindle_connect():
            context = pyudev.Context()
            monitor = pyudev.Monitor.from_netlink(context)
            monitor.filter_by(subsystem='block')
            for action, device in monitor:
                if ((device.get('ID_FS_LABEL')=='Kindle') & (action == 'change')):
                    print("Kindle Connected..")
                    helloMsg.setText("Kindle Connected")
                    return 1;
                if ((device.get('ID_FS_LABEL')=='Kindle') & (action == 'remove')):
                    print("Kindle Disconnected..")
                    helloMsg.setText("Reconnect Kindle")
                    return 0;
        
        def connection_stat():
            connectionThread = Thread(target=kindle_connect, daemon=True)
            connectionThread.start()

        def getdir():
            dirname = str(QFileDialog.getExistingDirectory())
            dirLine.setText(dirname)
            return dirname

        def process_file():
            for n in range(101):
                progress.setValue(n)
            x = dirLine.text()
            find_and_rename(x)
            helloMsg.setText("Books Transfered!")






        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle('Kindle Thumbnail Fix')
        
        helloMsg = QLabel("Please Reconnect Kindle", parent=window)
        helloMsg.move(200, 150)

        progress = QProgressBar(parent=window)
        progress.setValue(0)
        progress.setGeometry(QtCore.QRect(30, 200, 440, 20))

        dirLine = QLineEdit("Select Calibre Librebry Directory", parent=window)
        dirLine.setGeometry(QtCore.QRect(30, 230, 440, 20))
        
        loader = QLabel(parent=window)
        loader.setGeometry(QtCore.QRect(220, 25, 100, 100))
        movie = QMovie("connected.gif")
        loader.setMovie(movie)
        movie.start()


        layout = QHBoxLayout()
        button1 = QPushButton('Select Folder')
        button1.clicked.connect(getdir)
        button2 = QPushButton('Send To Kindle')
        button2.clicked.connect(process_file)
        layout.addWidget(button1)
        layout.addWidget(button2)
        window.setLayout(layout)
        window.setGeometry(100, 100, 500, 550)
        window.move(400,700)
        connection_stat()
        
        window.show()

        sys.exit(app.exec())




app()






