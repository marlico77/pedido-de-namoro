import tkinter as tk
from tkinter import messagebox
import random

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo('Love Box', 'Linda!')

def denied():
    button_1.destroy()

root = tk.Tk()
root.title('')
root.geometry('600x600')
root.configure(background='#4169E1')

margin = tk.Canvas(root, width=500, bg='#1C1C1C', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()

text_id = tk.Label(root, bg='#1C1C1C', text='Quer namorar comigo?', fg='#6A5ACD', font=('Montserrat', 24, 'bold'))
text_id.pack()

button_1 = tk.Button(root, text='Não', bg='#2E8B57', command=denied, relief='ridge', bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
root.bind('<Motion>', move_button_1)

button_2 = tk.Button(root, text='Sim', bg='#2E8B57', relief='ridge', bd=3, command=accepted, font=('Montserrat', 14, 'bold'))
button_2.pack()

root.mainloop()
