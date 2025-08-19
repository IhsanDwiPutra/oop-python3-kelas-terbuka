# Latihan OOP tkinter

import tkinter as tk

main_window = tk.Tk()

label1 = tk.Label(main_window, text="Hello World1")
label2 = tk.Label(main_window, text="Hello World2")

tombol1 = tk.Button(main_window, text="Klik Saya").pack()
tombol2 = tk.Button(main_window, text="Klik saya lagi").pack()

# method positioning
label1.pack()
label2.pack()

# method menampilkan GUI
main_window.mainloop()