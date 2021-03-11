import tkinter as tk

main_window = tk.Tk()

new_button = tk.Button(main_window, text="New")
new_button.grid(row=0, column=0, sticky="N")
exit_button = tk.Button(main_window, text='Exit')
exit_button.grid(row=0, column=1, sticky="N")

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)

main_window.title("15")
main_window.mainloop()
