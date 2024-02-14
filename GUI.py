import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()

        self.setGeometry(500,500,500,200)
        self.setWindowTitle("Desktop Refresh")


        self.Layout = QVBoxLayout()

        TitleLabel = QLabel("Desktop Refresh")
        TitleLabel.setObjectName('TitleHeader')
        self.Layout.addWidget(TitleLabel)
        TitleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.ButtonEvents = self.ButtonEvents()
        self.DisplayButtons()

        self.SetStyleSheet()

    def SetStyleSheet(self):
        with open('StyleSheet.qss', 'r') as File:
            Styles = File.read()
            self.setStyleSheet(Styles)



    def DisplayButtons(self):

        RefreshButton = QPushButton("Refresh", self)
        RefreshButton.setObjectName('RefreshButton')
        RefreshButton.clicked.connect(self.ButtonHandler)
        #RefreshButton.setGeometry(250,250,100,50)
        self.Layout.addWidget(RefreshButton)


        ConfigButton = QPushButton("Config", self)
        ConfigButton.setObjectName('ConfigButton')
        ConfigButton.clicked.connect(self.ButtonHandler)
        #ConfigButton.setGeometry(250,350,100,50)
        self.Layout.addWidget(ConfigButton)

        ButtonWidget = QWidget()
        ButtonWidget.setLayout(self.Layout)
        self.setCentralWidget(ButtonWidget)


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
            print("Refresh Button Event")

        def ConfigButtonEvent(self):
            print("Config Button Event")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
