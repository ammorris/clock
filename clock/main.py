import tkinter as tk
import random as r

from time import strftime

window = tk.Tk()
window.title("Time")
window.resizable(False, False)
window.attributes("-topmost", 1, "-alpha", 0.6)
window.iconbitmap("Shrimp.ico")

def time():
	date_time_format = strftime("%I:%M:%S\t%p\n%A, %B %d, %Y\nDay of the Year: %j")
	current_second = int(strftime("%S"))
	if current_second % 10 == 0:
		label["background"] = changeHexColor(label["background"])
	label.config(text=date_time_format)
	label.after(1000, time)

def changeHexColor(hex_color):
	dec_color = int(hex_color[1::], 16)
	new_color = str(hex(dec_color // 3)[2::])
	while len(new_color) < 6:
		new_color = r.choice(["A","C","F","0","3","5"]) + new_color
	return "#" + new_color

label = tk.Label(window, font=("ds-digital", 50), background="#ffff00", foreground="black")
label.pack(anchor="center")
time()

window.mainloop()