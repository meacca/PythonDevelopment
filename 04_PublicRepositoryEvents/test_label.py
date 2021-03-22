import tkinter as tk
from LabelEdit import InputLabel


class Application(tk.Frame):
    def __init__(self, master=None, title="<application>", **kwargs):
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        self.L = InputLabel(self)
        self.L.grid(row=0)
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        self.Q.grid(row=1)


app = Application(title="Test Input Label")
app.mainloop()