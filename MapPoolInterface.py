#Victor Stolle MapPoolInterface.py

from Tkinter import *
from MapToHTML import HTMLGenerator
from PIL import ImageTk, Image
from MapTocsv import CSVGenerator
class MapPoolInterface:


    '''
    Usage: m = MapPoolInterface()

    '''

    def __init__(self):

        self.counter = 0
        self.htmlgen = HTMLGenerator()
        self.allmaps = self.htmlgen.get_maps()
        self.toCSV = CSVGenerator(self.htmlgen.get_maps(), 'swiss.csv', self.htmlgen.get_sizes())

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
        self.run_button.config(height = 5, width = 30)
        self.test_button = Button(self.root, text = "Test", command = self.test_run)
        self.test_button.config(height = 5, width = 30)
        self.exit_button = Button(self.root, text = "Exit", command = self.byebye)
        self.exit_button.config(height = 5, width = 30)


        self.exit_button.pack(side = "bottom")

        self.panel.pack(side = "bottom", fill = "x", expand = 1)

        self.run_button.pack(side = "left", expand = 1)

        self.test_button.pack(side = "right", expand = 1)
        
        #Redirects the text from the console to the textbox
        sys.stdout = TextRedirector(self.text, "cout")


    
    def test_run(self):
        self.text.delete('1.0', END)
        self.htmlgen.run()


    def run_func(self):
        self.text.delete('1.0', END)
        self.htmlgen.run()
        self.run_button.destroy()
        self.test_button.destroy()
        self.text.config(state = DISABLED)
        self.toCSV.write()

    def byebye(self):
        self.root.destroy()
    
    def run(self):
        self.root.mainloop()



class TextRedirector(object):
    def __init__(self, widget, tag="cout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.insert("end", str, (self.tag,))




if __name__ == "__main__":

    m = MapPoolInterface()

    m.run()
