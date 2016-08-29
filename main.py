import threading
import queue
import time
from guroops import *
import graphics


def background_worker(out_q):
    while True:
        dic = Guroop().make_Dictionary()
        out_q.put(dic)
        print(dic)
        time.sleep(0.25)
    out_q.put("STOP")


def graphicsHandler(in_q):
    g = graphics.Graphics()
    print("GRAPHICS DONE")
    while True:
        data = in_q.get()
        g.create_random_circle(10, 3)



if __name__ == '__main__':

    try:
        # Create the shared queue and launch both threads
        q = queue.Queue()

        t = threading.Thread(target=background_worker, args=(q,))

        t.start()

        graphicsHandler(q)
    except:
        print("Error: Unable to start threads!")
    while 1:
        pass
