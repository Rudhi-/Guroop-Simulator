from tkinter import *


# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        # The "<Configure>" means that call on_resize if the size of the widget is changed
        self.bind("<Configure>", self.on_resize)
        # Updating height and width with current window's size
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        # self.scale("all",0,0,wscale,hscale)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def create_circle(self, x, y, r, **kwargs):
        self.create_rectangle(x - r, y - r, x + r, y + r, **kwargs)


def main():
    root = Tk()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe, width=850, height=400, bg="red", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)

    # add some widgets to the canvas
    mycanvas.create_line(0, 0, 200, 100)
    mycanvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
    mycanvas.create_rectangle(50, 25, 150, 75, fill="blue")

    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    root.mainloop()
