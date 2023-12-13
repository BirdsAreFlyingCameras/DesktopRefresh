"""
Desktop Refresh | Setup File

Author: Bryan Brannan

GitHub: BirdsAreFlyingCameras
"""


import sqlite3

class Setup:

    def __init__(self):
        self.DB = sqlite3.connect('Settings.sqlite3')

    def CreateTable(self):
        self.Cursor = self.DB

        self.Cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Settings (
            BaseDir TEXT,
            StorageDir TEXT
            )
            '''
        )
        self.DB.commit()

    def UserConfig(self):
        self.UserBaseDir = 'C:\\DesktopRefreshTestDir\\BaseDir'
        self.UserStorageDir = 'C:\\DesktopRefreshTestDir\\StorageDir'

        self.Cursor.execute(

            """
            INSERT INTO Settings (BaseDir, StorageDir) VALUES (?,?)""", (self.UserBaseDir, self.UserStorageDir)
)
        self.DB.commit()

Setup = Setup()

if __name__ == '__main__':
    Setup.CreateTable()
    Setup.UserConfig()
