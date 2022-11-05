import tkinter as tk
from app.ui import MainFrame
 
 
class App(tk.Tk):
 
    def __init__(self):
        super().__init__()
        self.config()
   
    def config(self):
        # configure the root window
        self.title('MyApp')
 
        # width and height
        window_height = 100
        window_width = 300
 
        # get window width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
 
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2)) - 80
        # set window geometry
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
 
# start
if __name__ == "__main__":
    # app instance
    app = App()
    frame = MainFrame(app)
    app.mainloop()
