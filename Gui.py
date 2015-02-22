__author__ = 'steven'
from tkinter import *
from tkinter import ttk
from helper.Logger import Logger

class Gui():

    def __init__(self):
        self.logger = Logger()
        self.logger.info("Initialising Gui class")

    def add(self):
        print(self.method.get())


    def Create_Gui_Objects(self):
        self.root = Tk()

        self.root.title("Batch HTTP Requester")
        self.input_label = ttk.Label(self.root, text="Url:")
        self.input = ttk.Entry(self.root)
        self.add = ttk.Button(self.root, text="Add", command=self.add)
        self.addfomfile = ttk.Button(self.root, text="Add from File")
        self.open_file = ttk.Button(self.root, text="Open File")
        self.columns_in_file = StringVar()
        self.columns_in_file = "-"
        self.values_in_file = ttk.Label(self.root, text=self.columns_in_file)
        self.headers_label = ttk.Label(self.root, text="Headers:")
        self.headers = ttk.Entry(self.root)
        self.body_label = ttk.Label(self.root, text="Body:")
        self.body = ttk.Entry(self.root)
        self.method_label = ttk.Label(self.root, text="Method")
        self.methodValues = StringVar()
        self.method = ttk.Combobox(self.root, textvariable=self.methodValues, state='readonly')
        self.method['values'] = ('GET', 'PUT', 'POST', 'DELETE')
        self.method.current(1)
        print(self.method.get())
        print(self.methodValues)


        self.method_label.grid(row=3, column=4, padx=10, pady=10)

        self.method.grid(row=3, column=5, padx=10, pady=10)
        self.body_label.grid(row=3, column=0, padx=10, pady=10)
        self.body.grid(row=3, column=1, padx=10, pady=10)
        self.input_label.grid(row=1, column=0, padx=10, pady=10)
        self.headers_label.grid(row=2, column=0, padx=10, pady=10)
        self.headers.grid(row=2, column=1, padx=10, pady=10)
        self.addfomfile.grid(row=1, column=5, padx=10, pady=10)
        self.open_file.grid(row=2, column=4, padx=10, pady=10)
        self.values_in_file.grid(row=2, column=5, padx=10, pady=10)
        self.input.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        self.add.grid(row=1, column=4, padx=10, pady=10)

        self.root.mainloop()
        print(self.method.get())






if __name__ == '__main__':
    gui = Gui()
    gui.Create_Gui_Objects()