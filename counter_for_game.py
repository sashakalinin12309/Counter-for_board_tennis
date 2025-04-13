# python 3.12.2
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def check_winn(name_winner: str, my_textvariable_point: tk.IntVar, neighbor_textvariable_point: tk.IntVar, textvariable_sets: tk.StringVar):

    my_textvariable_point.set(my_textvariable_point.get() + 1)

    my_counter = my_textvariable_point.get()
    neighbor_counter = neighbor_textvariable_point.get()

    if my_counter > 10 and my_counter - neighbor_counter > 1:

        messagebox.showinfo(message="Сет за {name}!".format(name=name_winner))
        print(textvariable_sets.get())
        new_value = textvariable_sets.get()[:-1] + str(int(textvariable_sets.get()[-1]) + 1)
        textvariable_sets.set(new_value)

        if int(textvariable_sets.get()[-1]) == 2:

            messagebox.showinfo(message="{name_command} победила по результатам сетов!".format(name_command=name_winner))

        my_textvariable_point.set(0)
        neighbor_textvariable_point.set(0)

        
tk.Button(text="restart", command=lambda: (counter_point1.set(0), counter_point2.set(0), counter_sets1.set("Выигранные сеты у red_command: 0"), counter_sets2.set("Выигранные сеты у blue_command: 0"))).pack(fill="both", expand=True)

counter_point1 = tk.IntVar(root, value=0)
counter_point2 = tk.IntVar(root, value=0)
counter_sets1 = tk.StringVar(root, value="Выигранные сеты у red_command: 0")
counter_sets2 = tk.StringVar(root, value="Выигранные сеты у blue_command: 0")

tk.Label(textvariable=counter_sets1).pack(fill="both", expand=1)
tk.Label(textvariable=counter_sets2).pack(fill="both", expand=True)

player1 = tk.Button(root, font="Arial 24", bg="red", activebackground="red", textvariable=counter_point1, command=lambda: check_winn("red_command", counter_point1, counter_point2, counter_sets1))
player1.pack(fill="both", expand=True)
player2 = tk.Button(root, font="Arial 24", bg="blue", activebackground="blue", textvariable=counter_point2, command=lambda: check_winn("blue_command", counter_point2, counter_point1, counter_sets2))
player2.pack(fill="both", expand=True)

root.mainloop()