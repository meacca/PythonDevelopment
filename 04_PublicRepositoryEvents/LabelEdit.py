import tkinter as tk


class InputLabel(tk.Label):
    def __init__(self, master):
        self.S = tk.StringVar("")
        self.fontsize = 10
        super().__init__(master, textvar=self.S, font=("TkFixedFont", self.fontsize), relief="sunken",
                         highlightthickness=1)
        self.F = tk.Frame(self, height=20, width=1, bg="black")

        self.cursor_position = 0
        self.bind("<KeyPress>", self.keypress_handler)
        self.bind("<Button-1>", self.buttonpress_handler)
        self.focus()

    def move_cursor(self, new_pos):
        self.cursor_position = max(min(new_pos, len(self.S.get())), 0)
        self.F.place(x=self.fontsize * self.cursor_position)
        self.focus()

    def add_symbol(self, char):
        old_string = self.S.get()
        new_string = old_string[:self.cursor_position] + char + old_string[self.cursor_position:]
        self.S.set(new_string)
        self.move_cursor(self.cursor_position+1)

    def delete_symbol(self):
        old_string = self.S.get()
        new_string = old_string[:max(self.cursor_position - 1, 0)] + old_string[self.cursor_position:]
        self.S.set(new_string)
        self.move_cursor(self.cursor_position-1)

    def keypress_handler(self, event):
        if event.char.isprintable():
            self.add_symbol(event.char)
        elif event.keysym == "Right":
            self.move_cursor(self.cursor_position+1)
        elif event.keysym == "Left":
            self.move_cursor(self.cursor_position-1)
        elif event.keysym == "Home":
            self.move_cursor(0)
        elif event.keysym == "End":
            self.move_cursor(len(self.S.get()))
        elif event.keysym == "BackSpace":
            self.delete_symbol()

    def buttonpress_handler(self, event):
        self.focus()
        self.move_cursor(event.x // self.fontsize)
