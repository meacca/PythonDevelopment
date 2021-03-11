import tkinter as tk


def generate_dummy_number_buttons(window):
    for i in range(15):
        row = i // 4 + 1
        column = i % 4
        text = str(i + 1)
        new_number = tk.Button(window, text=text)
        new_number.grid(row=row, column=column)


main_window = tk.Tk()

new_button = tk.Button(main_window, text="New")
new_button.grid(row=0, column=0, columnspan=2, sticky="N")
exit_button = tk.Button(main_window, text='Exit')
exit_button.grid(row=0, column=2, columnspan=2, sticky="N")
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)

generate_dummy_number_buttons(main_window)

main_window.title("15")
main_window.mainloop()
