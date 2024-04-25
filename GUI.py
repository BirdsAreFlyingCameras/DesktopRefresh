import tkinter
import customtkinter
from main import Main as FileSort
from tkinter import filedialog
from Config import Config


CT = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")


class MainWindow(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.WindowHeight = 300
        self.WindowWidth = 510

        self.geometry(f"{self.WindowWidth}x{self.WindowHeight}")
        self.title("Desktop Refresh")


        TitleLabelFont = customtkinter.CTkFont(family="Roboto", size=50, weight="bold")


        TitleLabel = customtkinter.CTkLabel(master=self, text="Desktop Refresh", fg_color="transparent",
                                            font=TitleLabelFont,justify="center")

        TitleLabel.place(relx=0.5, rely=0.2, anchor='center')


        self.ButtonEvents()
        self.Buttons()
        self.mainloop()

    def Buttons(self):

        self.ButtonHeight = 50
        self.ButtonWidth = 450

        self.ButtonFrameHeight = int((self.WindowHeight/3)*2)
        self.ButtonFrameWidth = self.ButtonWidth
        self.ButtonFrame = customtkinter.CTkFrame(master=self, height=int(self.ButtonFrameHeight), width=int(self.ButtonFrameWidth))
        self.ButtonFrame.configure(fg_color="transparent")
        self.ButtonFrame.grid(row=2, column=0, stick="nsew")


        ButtonFont = customtkinter.CTkFont(family="Roboto", size=30, weight="bold")


        RefreshButton = customtkinter.CTkButton(master=self.ButtonFrame, text="Refresh", height= self.ButtonHeight,
                                                width=self.ButtonWidth, font=ButtonFont, command=self.RefreshButtonEventCall)
        RefreshButton.grid(row=1)


        SettingsButton = customtkinter.CTkButton(master=self.ButtonFrame, text="Settings", height=self.ButtonHeight,
                                                 width=self.ButtonWidth, font=ButtonFont, command=self.SettingsButtonEventCall)
        SettingsButton.grid(row=2,pady=20)


        self.ButtonFrame.place(x=int((self.WindowWidth - self.ButtonFrameWidth)/2), y=int((self.ButtonFrameHeight/2) + self.WindowHeight/9))


    def ButtonEvents(self):
        def RefreshButtonEvent():
            FileSort.Start()

        def SettingsButtonEvent():
            self.SettingsWindow = SettingsWindow(self)
            self.SettingsWindow.grid()

        self.RefreshButtonEventCall = RefreshButtonEvent
        self.SettingsButtonEventCall = SettingsButtonEvent


class SettingsWindow(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowHeight = 300
        self.WindowWidth = 510
        self.configure(width=self.WindowWidth, height=self.WindowHeight)

        TitleLabelFont = customtkinter.CTkFont(family="Roboto", size=50, weight="bold")


        TitleLabel = customtkinter.CTkLabel(master=self, text="Settings", fg_color="transparent",
                                            font=TitleLabelFont,justify="center")

        TitleLabel.place(relx=0.5, rely=0.2, anchor='center')


        self.SavePathEntry = customtkinter.StringVar(self,"C:\\Save-Path-Name-Here")


        self.ItemFrameHeight = int((self.WindowHeight/3)*2)
        self.ItemFrameWidth = 450
        self.ItemFrame = customtkinter.CTkFrame(master=self, height=int(self.ItemFrameHeight), width=int(self.ItemFrameWidth))
        self.ItemFrame.configure(fg_color="transparent")
        self.ItemFrame.grid(row=3, column=0, stick="nsew")




        self.ButtonFont = customtkinter.CTkFont(family="Roboto", size=30, weight="bold")

        self.ButtonEvents()
        self.Buttons()
        self.Inputs()


    def Inputs(self):
        pass

    def Buttons(self):

        self.ButtonHeight = 50
        self.ButtonWidth = 450


        self.BasePathEntryButton = customtkinter.CTkButton(master=self.ItemFrame, text="Choose Base File Path",
                                                           height=self.ButtonHeight,
                                                           width=self.ButtonWidth, font=self.ButtonFont,
                                                           command=self.BasePathEntryButtonCall)

        self.BasePathEntryButton.grid(row=1)


        self.StoragePathEntryButton = customtkinter.CTkButton(master=self.ItemFrame, text="Choose Storage File Path",
                                                           height=self.ButtonHeight,
                                                           width=self.ButtonWidth, font=self.ButtonFont,
                                                           command=self.StoragePathEntryButtonCall)

        self.StoragePathEntryButton.grid(row=2)


        BackButton = customtkinter.CTkButton(master=self.ItemFrame, text="Back To Main Menu", height=self.ButtonHeight,
                                                 width=self.ButtonWidth, font=self.ButtonFont,
                                                 command=self.BackButtonEventCall)
        BackButton.grid(row=3)



        self.ItemFrame.place(x=int((self.WindowWidth - self.ItemFrameWidth)/2), y=int((self.ItemFrameHeight/2) + self.WindowHeight/9))


    def ButtonEvents(self):
        def BackButtonEvent():
            self.destroy()
        self.BackButtonEventCall = BackButtonEvent
        def BasePathEntryButton():
            tkinter.Tk().withdraw()
            FolderPath = filedialog.askdirectory()
            Config.PathConfig(BaseDir=FolderPath)

        self.BasePathEntryButtonCall = BasePathEntryButton

        def StoragePathEntryButton():
            tkinter.Tk().withdraw()
            FolderPath = filedialog.askdirectory()
            Config.PathConfig(StorageDir=FolderPath)

        self.StoragePathEntryButtonCall = StoragePathEntryButton


MainWindow()
