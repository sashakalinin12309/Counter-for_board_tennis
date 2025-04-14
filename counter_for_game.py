# python 3.12.2
# Импортируем необходимые модули.
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()  # Создаем главное окно.

def check_winn(name_winner: str, my_textvariable_point: tk.IntVar, neighbor_textvariable_point: tk.IntVar, textvariable_sets: tk.StringVar):

    """
    Функция добавляет +1 очко игроку и проверяет на выигрушную позицию.
    Если игрок выиграл сет или игру в целом, 
    то программа оповещает об этом игрока.

    Аргументы:
    - name_winner: str - имя игрока, который только что получил очко;
    - my_textvariable_point: tk.IntVar - текстовый виджет с информацией об очках name_winner;
    - neighbor_textvariable_point: tk.Intvar - текстовый виджет с информацией об очках противника;
    - textvariable_sets: tk.StringVar - текстовый виджет с кол-вом выигранных сетов у name_winner.

    В конце:
        Программа добавляет очко name_winner и проверяет на победную позицию.  
    """

    my_textvariable_point.set(my_textvariable_point.get() + 1)  # Добавляем очко только что забившему.

    my_counter: int = my_textvariable_point.get()  # Кол-во очков у нас в int типе.
    neighbor_counter: int = neighbor_textvariable_point.get()  # Кол-во очков у противника в int типе.

    # Проверка на выполнение условий выигрыша.
    if my_counter > 10 and my_counter - neighbor_counter > 1:

        messagebox.showinfo(message="Сет за {name}!".format(name=name_winner))  # Выводим сообщение о победе сета.
        new_value = textvariable_sets.get()[:-1] + str(int(textvariable_sets.get()[-1]) + 1)  # Новое значение о кол-вах выигранных сетов (+1)
        textvariable_sets.set(new_value)  # Запоминаем о выигрыше сета.

        if int(textvariable_sets.get()[-1]) == 2:  # Если игрок выиграл два сета (победил то есть).

            # Выводим сообщение о выигрыше name_winner.
            messagebox.showinfo(message="{name_command} победила по результатам сетов!".format(name_command=name_winner))

        # Так как сет закончился, нужно обнулить результаты игроков.
        my_textvariable_point.set(0)  
        neighbor_textvariable_point.set(0)
        
# Кнопка для перезапуска игры.
tk.Button(text="restart", command=lambda: (counter_point1.set(0), counter_point2.set(0), counter_sets1.set("Выигранные сеты у red_command: 0"), counter_sets2.set("Выигранные сеты у blue_command: 0"))).pack(fill="both", expand=True)

counter_point1 = tk.IntVar(root, value=0)  # Счетчик очков player1.
counter_point2 = tk.IntVar(root, value=0)  # Счетчик очков player2.
counter_sets1 = tk.StringVar(root, value="Выигранные сеты у red_command: 0")  # Счетчик выигранных сетов у player1.
counter_sets2 = tk.StringVar(root, value="Выигранные сеты у blue_command: 0")  # Счетчик выигранных сетов у player2.

tk.Label(textvariable=counter_sets1).pack(fill="both", expand=1)  # Виджет показывает counter_sets1.
tk.Label(textvariable=counter_sets2).pack(fill="both", expand=1)  # Виджет показывает counter_sets2.

# Виджет показывает counter_point1.
player1 = tk.Label(root, font="Arial 24", bg="red", textvariable=counter_point1)     
player1.pack(fill="both", expand=True)

# Кнопки для увеличения/уменьшения очков у player1. 
tk.Button(player1, font="Arial 12", bg="red", activebackground="red", text="+", width=1, command=lambda: check_winn("red_command", counter_point1, counter_point2, counter_sets1)).pack(anchor="ne", fill="y", expand=1)
tk.Button(player1, font="Arial 12", bg="red", activebackground="red", text="-", width=1, command=lambda: counter_point1.set(counter_point1.get()-1)).pack(anchor="se", fill="y", expand=1)

# Виджет показывает counter_point2.
player2 = tk.Label(root, font="Arial 24", bg="blue", textvariable=counter_point2)
player2.pack(fill="both", expand=True)

# Кнопки для увеличения/уменьшения очков у player2. 
tk.Button(player2, font="Arial 12", bg="blue", activebackground="blue", text="+", width=1, command=lambda: check_winn("blue_command", counter_point2, counter_point1, counter_sets2)).pack(anchor="ne", fill="y", expand=1)
tk.Button(player2, font="Arial 12", bg="blue", activebackground="blue", text="-", width=1, command=lambda: counter_point2.set(counter_point2.get()-1)).pack(anchor="se", fill="y", expand=1)

root.mainloop()  # Обработка всех событий.