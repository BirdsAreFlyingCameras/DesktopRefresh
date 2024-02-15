import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from main import Main

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()

        self.setGeometry(500,500,500,200)
        self.setWindowTitle("Desktop Refresh")

        self.BaseMenu = BaseMenu(self)
        self.ConfigMenu = ConfigMenu(self)



        self.StackedWidget = QStackedWidget()


        self.StackedWidget.addWidget(self.BaseMenu)
        self.StackedWidget.addWidget(self.ConfigMenu)

        self.setCentralWidget(self.StackedWidget)

    def SwitchWindows(self, WindowName):

        if WindowName == "ConfigWindow":
            self.StackedWidget.setCurrentWidget(self.ConfigMenu)

        if WindowName == "MainMenu":
            self.StackedWidget.setCurrentWidget(self.BaseMenu)


class BaseMenu(QWidget):
    def __init__(self, MainWindow):
        super().__init__()

        self.MainWindow = MainWindow

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
            self.RefreshButtonEvent()

        if ButtonName == "ConfigButton":
            print("Config Button Handler Flag")
            self.ConfigButtonEvent()

    def RefreshButtonEvent(self):
        Main.Start()
        print("Refresh Button Event")

    def ConfigButtonEvent(self):
        print("Config Button Event")
        self.MainWindow.SwitchWindows(WindowName="ConfigWindow")

class ConfigMenu(QWidget):
    def __init__(self, MainWindow):
        super().__init__()

        self.MainWindow = MainWindow

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        TitleLabel = QLabel("Desktop Refresh")
        TitleLabel.setObjectName('TitleHeader')
        TitleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.layout.addWidget(TitleLabel)

        self.SetStyleSheet()
        self.DisplayButtons()

    def DisplayButtons(self):
        ReturnToMainMenuButton = QPushButton("Return To Main Menu", self)
        ReturnToMainMenuButton.setObjectName('MainMenuButton')
        ReturnToMainMenuButton.clicked.connect(self.ButtonHandler)
        self.layout.addWidget(ReturnToMainMenuButton)

    def ButtonHandler(self):
        sender = self.sender()  # Get the sender object
        ButtonName = sender.objectName()  # Get the object name of the sender
        print(f"Button clicked: {ButtonName}")

        if ButtonName == "MainMenuButton":
            print("Refresh Button Handler Flag")
            self.MainMenuButtonEvent()

    def MainMenuButtonEvent(self):
        print("Config Button Event")
        self.MainWindow.SwitchWindows(WindowName="MainMenu")
    def SetStyleSheet(self):
        with open('StyleSheet.qss', 'r') as File:
            Styles = File.read()
            self.setStyleSheet(Styles)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
