#Victor Stolle MapPoolInterface.py

from Tkinter import *
from MapPoolGenerator import MapPoolGenerator
from PIL import ImageTk, Image
class MapPoolInterface:


    '''
    Usage: m = MapPoolInterface()

    '''

    def __init__(self):

        self.counter = 0

        self.root = Tk()
        self.root.title("osu!UCI Summer League 2015")
        self.root.config(width = 800, height = 800)       

        #OSL Logo
        self.path = "OSL_background.jpg"
        self.img = ImageTk.PhotoImage(Image.open(self.path))

        #Display
        self.panel = Label(self.root, image = self.img)
        self.text = Text(self.root, bg = "#293134", foreground = "#C0C0C0", font = "Arial")

        #sidebar
        self.scroll = Scrollbar(self.root)
        self.scroll.pack(side="right", fill = "y")
        self.text.pack(side = "left", fill = "both", expand = 1)
        self.run_button = Button(self.root, text = "Run", command = self.run_func)
        self.exit_button = Button(self.root, text = "Exit", command = self.byebye)

        #Week Selector
        self.textRoot = Toplevel(self.root)
        self.textRoot.lift(aboveThis = self.root)
        self.textRoot.grid()
        self.weekText = Label(self.textRoot, text = "Please Enter the Week Number (1 - 10): ")
        self.weekEntry = Entry(self.textRoot)
        self.weekConfirm = Button(self.textRoot, text = "Enter", command=self.config)
        self.weekEntry.grid(column = 0, row = 1)
        self.weekConfirm.grid(column = 1, row = 1)
        self.weekText.grid(row = 0)
        self.run_button.grid(row = 0, column = 1)
        self.exit_button.grid(row = 1, column = 2)
        self.run_button.pack(side = "top")
        self.exit_button.pack(side = "bottom")
        self.panel.pack(side = "top", fill = "both", expand = 1)


        #Redirects the text from the console to the textbox
        sys.stdout = TextRedirector(self.text, "cout")



    def config(self):
        self.week = int(self.weekEntry.get())
        self.mpg = MapPoolGenerator(self.week)
        self.textRoot.destroy()
        
    def run_func(self):
        self.mpg.run()
        self.run_button.destroy()


    def byebye(self):
        self.root.destroy()
    
    def run(self):
        self.root.mainloop()



class TextRedirector(object):
    def __init__(self, widget, tag="cout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")



if __name__ == "__main__":

    m = MapPoolInterface()

    m.run()
