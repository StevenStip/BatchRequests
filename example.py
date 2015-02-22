__author__ = 'steven'


__author__ = 'steven.van.stiphout'
from tkinter import *
from tkinter import filedialog
import queue
import requests
import threading


class ThreadedHttpWorker():

    messages = []

    def worker(self, q, callback):
        q_filled = True
        while q_filled:
            try:
                Id = q.get(False)
                callback(**Id)

            except queue.Empty:
                q_filled = False

    def DoFromList(self, task_list, callback):
        """
        column=0 => customers
        column=1 => devices"""
        q = queue.Queue()

        for item in task_list:  #iterate over the file one line at a time (memory efficient)
            print(item)
            q.put(item)

        thread_count = 16
        for i in range(thread_count):
            t = threading.Thread(target=self.worker, args=(q, callback))
            t.start()
        #make the main thread wait till all the threads are done
        for t in threading.enumerate():
            if t is not threading.currentThread():
                t.join()

    def DoCall(self, method, url="", body="", header={}):
        print(method)
        print(url)
        r = requests.Response

        if method == "get":
            r = requests.get(url=url, headers=header)

        if method == "put":
            r = requests.put(url=url, headers=header, body=body)

        print(r.status_code)


class GuiHelper():

    def __init__(self):
        self.file_path = None
        self.httpworker = ThreadedHttpWorker()



    def ReadFile(self):
        #self.file_path = askopenfilename(parent=self.root)
        self.file_path = filedialog.askopenfilename(parent=self.root)
        with open(self.file_path) as f:
            for line in f:  #iterate over the file one line at a time (memory efficient)
                #remove newline at the end
                line = line.rstrip('\n')
                list = line.split(", ")
                self.v.set(str(len(list)))
        print(self.file_path)
        #messages.append({"method":"get", "url":"http://www.nu.nl"})
        #messages.append({"method":"get", "url":"http://www.google.nl"})
        self.httpworker.DoFromList(self.httpworker.messages, self.httpworker.DoCall)


    def AddJob(self):
        url= "http://"+self.e1.get().lstrip("http://")
        user_agent = self.e2.get()
        print("Adding: "+url)
        self.httpworker.messages.append({"method":"get", "url":url, "header":{'User-agent': user_agent}})

    def AddJobsFromFile(self):
        url_input = self.e1.get()
        user_agent_input = self.e2.get()
        if url_input == "":
            return
        with open(self.file_path) as f:
            for line in f:  #iterate over the file one line at a time (memory efficient)
                #remove newline at the end
                line = line.rstrip('\n')
                list = line.split(", ")
                url = "http://"+url_input.lstrip("http://").format(*list)
                user_agent = user_agent_input.format(*list)
                self.httpworker.messages.append({"method":"get", "url":url, "header":{'User-agent': user_agent}})
        return

    def main(self):

        self.httpworker = ThreadedHttpWorker()
        self.root = Tk()
        self.root.geometry()
        self.e1 = Entry()
        self.v = StringVar()
        self.Lb1 = Label(self.root, textvariable=self.v)
        self.B1 = Button(self.root, text="Execute", command=lambda: self.httpworker.DoFromList(self.httpworker.messages, self.httpworker.DoCall))
        self.B2 = Button(self.root, text="add", command=self.AddJob)
        self.B3 = Button(self.root, text="Open File", command=self.ReadFile )
        self.B4 = Button(self.root, text="Create Jobs based on File", command=self.AddJobsFromFile)
        self.e2 = Entry()
        #self.Lb2 = Tkinter.Label()

        self.e2.grid(row=1, column=0, padx=10, pady=10)
        self.Lb1.grid(row=2, column=2, padx=10, pady=10)
        self.B1.grid(row=1, column=1, padx=10, pady=10)
        self.B2.grid(row=0, column=1, padx=10, pady=10)
        self.B3.grid(row=2, padx=10, pady=10)
        self.B4.grid(row=2, column=1, padx=10, pady=10)
        self.e1.grid(row=0, column=0, padx=10, pady=10)

        self.root.mainloop()

if __name__ == '__main__':
    Gui = GuiHelper()
    Gui.main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          