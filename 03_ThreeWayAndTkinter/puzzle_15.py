import tkinter as tk


def generate_dummy_number_buttons(window):
    for i in range(15):
        row = i // 4 + 1
        column = i % 4
        text = str(i + 1)
        new_number = tk.Button(window, text=text)
        new_number.grid(row=row, column=column, sticky="NEWS")


def configure_row_columns(window):
    for column in range(0, 4):
        window.columnconfigure(column, weight=1)
    for row in range(1, 5):
        window.rowconfigure(row, weight=1)



main_window = tk.Tk()

new_button = tk.Button(main_window, text="New")
new_button.grid(row=0, column=0, columnspan=2, sticky="N")
exit_button = tk.Button(main_window, text='Exit')
exit_button.grid(row=0, column=2, columnspan=2, sticky="N")

generate_dummy_number_buttons(main_window)
configure_row_columns(main_window)

main_window.title("15")
main_window.mainloop()
