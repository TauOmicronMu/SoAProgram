from Tkinter import *
from TimeStamp import *
from logging import *
from Constants import *
from CreatePopup import *

from Strings import *

class MainScreen(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent

        self.initialiseUI()
        
    def initialiseUI(self):

        Image = PhotoImage(file=LOGO_FILENAME)
        global label
        label = Label(self.parent, image=Image, relief=RAISED)
        label.image = Image
        label.pack()
    
        self.parent.title(WINDOW_TITLE)
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        
        fileMenu.add_command(label=DROPDOWN_QUIT_TEXT, underline=0, command=self.Quit)

        fileMenu.add_separator()

        fileMenu.add_command(label=DROPDOWN_HELP_TEXT, underline=0, command=self.Help)

        fileMenu.add_separator()
        
        MainMenu = Menu(menubar)
        
        MainMenu.add_command(label=MENU_CREATE_TEXT, command=self.CreateRecord)
        MainMenu.add_command(label=MENU_SEARCH_TEXT, command=self.SearchRecords)
        MainMenu.add_cascade(label=MENU_AMEND_TEXT, command=self.AmendRecord)
        MainMenu.add_command(label=MENU_DELETE_TEXT)

        expMenu = Menu(menubar)
        
        menubar.add_cascade(label=MENUBAR_FILE_TEXT, underline=0, menu=fileMenu)
        menubar.add_cascade(label=MENUBAR_MENU_TEXT, underline=0, menu=MainMenu)
                
    def Quit(self):
        
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + QUIT_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + WINDOW_TERMINATED_TEXT)

    def Help(self):
        
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MAIN_SCREEN_HELP_SELECTED_TEXT)
            CreatePopup(MAIN_SCREEN_HELP_TEXT)

    def CreateRecord(self):
        pass

    def SearchRecords(self):
        pass

    def AmendRecord(self):
        pass

