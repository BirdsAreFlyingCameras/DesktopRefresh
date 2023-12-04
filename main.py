import os, datetime, shutil, pprint

import PyEnhance.Counter
from PyEnhance import *

pprint = pprint.pprint

datetime = datetime.datetime

Counter = PyEnhance.Counter.Counter

BaseDir = 'C:\\DesktopRefreshTestDir\\BaseDir'
StorageDir = 'C:\\DesktopRefreshTestDir\\StorageDir'


class Main:

    def __init__(self):
        self.BaseDir = 'C:\\DesktopRefreshTestDir\\BaseDir' # will change to pull from config database
        self.StorageDir = 'C:\\DesktopRefreshTestDir\\StorageDir' # will change to pull from config database
        self.Date = datetime.now()
        Date = self.Date
        self.StorageFileName = (f'{Date.month}-{Date.day}-{Date.year} ({Date.strftime("%I")}_{Date.strftime("%M")} {Date.strftime("%p")})')

        self.BaseDirFileList = []
        self.AllFileExtensionsList = [
            "jpg", "jpeg", "png", "gif", "bmp", "tiff", "ico", "webp", "svg", "eps",
            "mp3", "wav", "flac", "aac", "ogg", "wma", "m4a", "ac3", "mid", "midi",
            "mp4", "m4v", "avi", "mkv", "wmv", "mov", "flv", "webm", "mpg", "mpeg", "3gp", "rm", "rmvb", "swf", "vob",
            "ogv", "divx",
            "xls", "xlsx", "csv", "doc", "docx", "ppt", "pptx", "pdf", "txt", "rtf",
            "zip", "rar", "7z", "tar",
            "lnk"
        ]

        self.BaseDirFilesSorted = {
                                "Media":{"Images":[],"Audio":[], "Videos":[]},
                                "Documents":{"Spreadsheets":[], "Word-Files":[], "PDFs":[], "Text":[]},
                                "Archives":[],
                                "Shortcuts":[],
                                "Misc-Unsorted":[]

                                }

        self.FileExtensionsDict = {

            "Media":{
                "Images":["jpg", "jpeg", "png", "gif", "bmp", "tiff", "ico", "webp", "svg", "eps"],
                "Audio":[ "mp3", "wav", "flac", "aac", "ogg", "wma", "m4a", "ac3", "mid", "midi"],
                "Videos":["mp4", "m4v", "avi", "mkv", "wmv", "mov", "flv", "webm", "mpg", "mpeg", "3gp", "rm", "rmvb", "swf", "vob", "ogv", "divx"]
            },

            "Documents": {
                "Spreadsheets": ["xls", "xlsx", "csv"],
                "Office Files": ["doc", "docx", "ppt", "pptx"],
                "PDFs": ["pdf"],
                "Text": ["txt", "rtf"]
            },

            "Archives": ["zip", "rar", "7z", "tar"],

            "Shortcuts": ["lnk"]

        }

    def MakeTestFiles(self,FileTypesList=None, NestedFiles=None, BaseFileDir=None, Contained = None):
        BaseFileDir = str(BaseFileDir)
        FileTypes = list(FileTypesList)
        os.chdir(BaseFileDir)

        if Contained == True:

            if os.path.exists('TestFilesDir'):
                os.remove('TestFilesDir')

            os.mkdir('TestFilesDir')
            os.chdir('TestFilesDir')

            if NestedFiles == True:
                if os.path.exists('NestedTestDir'):
                    os.remove('NestedTestDir')
                os.mkdir("NestedTestDir")
                os.chdir("NestedTestDir")

        for FileType in FileTypes:
            FileType = str(FileType)

            if '.' in FileType:
                LastDotIndex = FileType.rindex('.')
                FileType = FileType[LastDotIndex + 1:]



            TestFileName = f"{FileType}-File.{FileType}"


            if os.path.exists(TestFileName):
                os.remove(TestFileName)


            with open(f'{TestFileName}', "x") as File:
                File.write(f'This is a {FileType} file')

    def Checks(self):

        Date = self.Date

        if not os.path.exists(BaseDir):
            print(f"{BaseDir} Is not a valid dir")
        else:
            print(f"Base Dir: {self.BaseDir}")


        if not os.path.exists(StorageDir):
            print(f"{StorageDir} is not a valid dir")
        else:
            print(f'Storage Dir: {self.StorageDir}')

        os.chdir(StorageDir)

        if os.path.exists(self.StorageFileName):
            self.StorageFileName = (f'{Date.month}-{Date.day}-{Date.year} ({Date.strftime("%I")}_{Date.strftime("%M")}_{Date.strftime("%S")} {Date.strftime("%p")})')

            if os.path.exists(self.StorageFileName):
                print("Please try again")

        os.chdir(BaseDir)

        print(f"Storage Name: {self.StorageFileName}")

        print("Checks Complete All good")

    def IndexFiles(self):
        Files = os.listdir(self.BaseDir)
        print('\n')



        for File in Files:

            if '.' not in File:
                print('String "." not in file name')
                #print(f'The file extension for {File} is {self.FileExtension}')

                # Add code to check if file is a folder

            else:
                LastDotIndex = File.rindex('.')
                self.FileExtension = File[LastDotIndex+1:]
                #print(f'The file extension for {File} is {self.FileExtension}')

            for category, subcategories in self.FileExtensionsDict.items():

                if self.FileExtension in self.FileExtensionsDict[category]:
                    self.BaseDirFilesSorted[category].append(File)

                if isinstance(subcategories, dict):
                    for subcategory in subcategories:
                        #print(self.FileExtensionsDict[category][subcategory])

                        if self.FileExtension in self.FileExtensionsDict[category][subcategory]:


                            self.BaseDirFilesSorted[category][subcategory].append(File)

            if self.FileExtension not in self.AllFileExtensionsList:
                self.BaseDirFilesSorted['Misc-Unsorted'].append(File)

        pprint(self.BaseDirFilesSorted)

                             #adding file sorting here!!!

    def StoreFiles(self):

        os.chdir(self.StorageDir)
        os.mkdir(self.StorageFileName)
        os.chdir(self.StorageFileName)



        for File in self.BaseDirFileList:
            print(f"Moving {File} to {self.StorageDir}\\{self.StorageFileName}")
            shutil.move(f"{BaseDir}\\{File}", f"{self.StorageDir}\\{self.StorageFileName}")



Main = Main()

if __name__ == '__main__':
    FileTypeList = ['txt', '.rtf', 'pdf', 'lnk', 'png', 'mp3', 'mp4']
    BaseDir = 'C:\\DesktopRefreshTestDir\\BaseDir'
    Main.MakeTestFiles(FileTypesList=FileTypeList, BaseFileDir=BaseDir, NestedFiles=False, Contained=False)


    Main.Checks()
    Main.IndexFiles()
    Main.StoreFiles()

