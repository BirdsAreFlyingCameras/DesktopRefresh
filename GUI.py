import tkinter
import customtkinter
from main import Main as FileSort




CT = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")


class Main:

    def __init__(self):

        self.WindowHeight = 300
        self.WindowWidth = 510

        CT.geometry(f"{self.WindowWidth}x{self.WindowHeight}")
        CT.title("Desktop Refresh")


        TitleLabelFont = customtkinter.CTkFont(family="Roboto", size=50, weight="bold")


        TitleLabel = customtkinter.CTkLabel(master=CT, text="Desktop Refresh", fg_color="transparent",
                                            font=TitleLabelFont,justify="center")

        TitleLabel.place(relx=0.5, rely=0.2, anchor='center')


        self.ButtonEvents()
        self.Buttons()
        CT.mainloop()

    def Buttons(self):

        self.ButtonHeight = 50
        self.ButtonWidth = 450

        self.ButtonFrameHeight = int((self.WindowHeight/3)*2)
        self.ButtonFrameWidth = self.ButtonWidth
        self.ButtonFrame = customtkinter.CTkFrame(master=CT, height=int(self.ButtonFrameHeight), width=int(self.ButtonFrameWidth))
        self.ButtonFrame.configure(fg_color="transparent")
        self.ButtonFrame.grid(row=2, column=0, stick="nsew")


        ButtonFont = customtkinter.CTkFont(family="Roboto", size=30, weight="bold")


        RefreshButton = customtkinter.CTkButton(master=self.ButtonFrame, text="Refresh", height= self.ButtonHeight,
                                                width=self.ButtonWidth, font=ButtonFont, command=self.RefreshButtonEventCall)
        RefreshButton.grid(row=1)


        SettingsButton = customtkinter.CTkButton(master=self.ButtonFrame, text="Settings", height=self.ButtonHeight,
                                                 width=self.ButtonWidth, font=ButtonFont)
        SettingsButton.grid(row=2,pady=20)


        self.ButtonFrame.place(x=int((self.WindowWidth - self.ButtonFrameWidth)/2), y=int((self.ButtonFrameHeight/2) + self.WindowHeight/9))

    def ButtonEvents(self):

        def RefreshButtonEvent():
            FileSort.Start()

        self.RefreshButtonEventCall = RefreshButtonEvent

Main()