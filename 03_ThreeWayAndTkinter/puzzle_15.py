import tkinter as tk
import random


def generate_random_number_buttons():
    global current_empty
    random_empty = random.randint(0, 15)
    random_seq = list(range(0, 15))
    random.shuffle(random_seq)
    cur_elem = 0
    for i in range(16):
        row = i // 4 + 1
        column = i % 4
        if i != random_empty:
            number_buttons[random_seq[cur_elem]].grid(row=row, column=column, sticky="NEWS")
            cur_elem += 1
    current_empty = random_empty


def configure_row_columns():
    for column in range(0, 4):
        main_window.columnconfigure(column, weight=1)
    for row in range(1, 5):
        main_window.rowconfigure(row, weight=1)


def number_click_action(number_idx):
    def custom_func():
        global current_empty
        empty_row, empty_column = current_empty // 4 + 1, current_empty % 4
        cur_row = number_buttons[number_idx].grid_info()["row"]
        cur_column = number_buttons[number_idx].grid_info()["column"]
        if abs(cur_row - empty_row) + abs(cur_column - empty_column) <= 1:
            number_buttons[number_idx].grid(row=empty_row, column=empty_column, sticky="NEWS")
            current_empty = (cur_row - 1) * 4 + cur_column % 4
    return custom_func


main_window = tk.Tk()
current_empty = 0
number_buttons = [tk.Button(main_window, text=str(i+1), command=number_click_action(i)) for i in range(15)]

generate_random_number_buttons()
configure_row_columns()

new_button = tk.Button(main_window, text="New", command=generate_random_number_buttons)
new_button.grid(row=0, column=0, columnspan=2, sticky="N")
exit_button = tk.Button(main_window, text='Exit', command=main_window.destroy)
exit_button.grid(row=0, column=2, columnspan=2, sticky="N")

main_window.title("15")
main_window.mainloop()
