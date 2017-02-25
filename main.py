import threading
import queue
import time
import guroops
import graphics


def background_worker(out_q):
    c =0
    while True:
        if c is 10:
            break
        dic = guroops.Guroop().make_Dictionary()
        out_q.put(dic)
        print(dic)
        time.sleep(0.25)
        c+=1
    out_q.put("STOP")


def graphicsHandler(in_q):
    g = graphics.Graphics()
    while True:
        data = in_q.get()
        g.create_random_circle(10, 3)
        if data is "STOP":
            print("STOPPED")
            break



if __name__ == '__main__':

    try:
        # Create the shared queue and launch both threads
        q = queue.Queue()
        t = threading.Thread(target=background_worker, args=(q,))
        t.start()
        graphicsHandler(q)
        t.join()
    except:
        print("Error: Unable to start threads!")
