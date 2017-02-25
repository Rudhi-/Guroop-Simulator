from tkinter import *
from rescalingcanvas import ResizingCanvas
import time
import random


class Graphics:
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=YES)
        self.canvas = ResizingCanvas(self.frame, width=1200, height=600, bg="silver", highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)

        # add some widgets to the canvas
        for x in range(10):
            # print("START")
            if self.create_random_circle(10, 3) == -1:
                break
        #print("DONE")
        #self.root.mainloop()
        self.root.update_idletasks()
        self.root.update()

    def create_random_circle(self, radius, sepdisance):
        timeout = time.time() + (60 * 0.05)  # 1.5 minutes from now
        color = ["red", "orange", "yellow", "green", "blue", "violet"]
        x = random.uniform(radius, self.canvas.getWidth() - radius)
        y = random.uniform(radius, self.canvas.getHeight() - radius)
        while len(
                self.canvas.find_overlapping(x - radius - sepdisance, y - radius - sepdisance, x + radius + sepdisance,
                                             y + radius + sepdisance)) >= 1:
            x = random.uniform(radius, self.canvas.getWidth() - radius)
            y = random.uniform(radius, self.canvas.getHeight() - radius)
            if time.time() >= timeout:
                print("TIMEOUT!")
                return -1
        if time.time() < timeout:
            circle = self.canvas.create_circle(x, y, radius, fill=random.choice(color))
        self.root.update_idletasks()
        self.root.update()