import tkinter as tk


class InputLabel(tk.Label):
    def __init__(self, master):
        self.S = tk.StringVar("")
        self.fontsize = 10
        super().__init__(master, textvar=self.S, font=("Courier", self.fontsize+2), relief="sunken")
        self.F = tk.Frame(self, height=20, width=1, bg="black")

        self.cursor_position = 0
        self.bind("<KeyPress>", self.keypress_handler)
        self.bind("<Button-1>", self.buttonpress_handler)

    def move_cursor(self, new_pos):
        self.cursor_position = max(min(new_pos, len(self.S.get())), 0)
        self.F.place(x=self.fontsize * self.cursor_position)

    def add_symbol(self, char):
        old_string = self.S.get()
        new_string = old_string[:self.cursor_position] + char + old_string[self.cursor_position:]
        self.S.set(new_string)
        self.move_cursor(self.cursor_position+1)

    def keypress_handler(self, event):
        if event.char.isprintable():
            self.add_symbol(event.char)

    def buttonpress_handler(self, event):
        self.focus()
        self.move_cursor(event.x // self.fontsize)
