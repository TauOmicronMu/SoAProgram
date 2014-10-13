from Tkinter import *
from Constants import *
from logging import *
from TimeStamp import *
from MainScreen import *

from Strings import *
from LoggingStrings import *

basicConfig(filename=LOG_FILENAME,level=DEBUG,)
    
def main():

    try:
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISING_WINDOW_TEXT + WINDOW_GEOMETRY + "\n") 
        app = MainScreen(root)
        root.mainloop()
    except:
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp(),)
        exception(GOT_MAIN_EXCEPTION)
        raise

if __name__ == '__main__':
    main()  #Main
