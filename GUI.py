import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from main import Main

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()

        self.setGeometry(500,500,500,200)
        self.setWindowTitle("Desktop Refresh")

        self.setCentralWidget(self.BaseMenu())


    class BaseMenu(QWidget):
        def __init__(self):
            super().__init__()

            self.ButtonEvents = self.ButtonEvents()

            self.layout = QVBoxLayout()
            self.setLayout(self.layout)

            TitleLabel = QLabel("Desktop Refresh")
            TitleLabel.setObjectName('TitleHeader')
            self.layout.addWidget(TitleLabel)
            TitleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

            self.SetStyleSheet()
            self.DisplayButtons()

        def SetStyleSheet(self):
            with open('StyleSheet.qss', 'r') as File:
                Styles = File.read()
                self.setStyleSheet(Styles)



        def DisplayButtons(self):

            RefreshButton = QPushButton("Refresh", self)
            RefreshButton.setObjectName('RefreshButton')
            RefreshButton.clicked.connect(self.ButtonHandler)
            self.layout.addWidget(RefreshButton)


            ConfigButton = QPushButton("Config", self)
            ConfigButton.setObjectName('ConfigButton')
            ConfigButton.clicked.connect(self.ButtonHandler)
            self.layout.addWidget(ConfigButton)

        def ButtonHandler(self):
            sender = self.sender()  # Get the sender object
            ButtonName = sender.objectName()  # Get the object name of the sender
            print(f"Button clicked: {ButtonName}")

            if ButtonName == "RefreshButton":
                print("Refresh Button Handler Flag")
                self.ButtonEvents.RefreshButtonEvent()

            if ButtonName == "ConfigButton":
                print("Config Button Handler Flag")
                self.ButtonEvents.ConfigButtonEvent()


        class ButtonEvents:
            def __init__(self):
                super(MainWindow).__init__()

            def RefreshButtonEvent(self):
                Main.Start()
                print("Refresh Button Event")

            def ConfigButtonEvent(self):
                print("Config Button Event")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
