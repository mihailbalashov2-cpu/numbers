import tkinter as tk
from PIL import Image, ImageTk
import func as f

win = tk.Tk()
win.title('Числовая угадайка')
win.config(bg='#c2c2c2')
win.geometry("500x600+100+200")
win.resizable(False, False)

#Получаем фото и меняем
img = Image.open('title.png')
image = ImageTk.PhotoImage(img)
win.iconphoto(False, image)
# Переменная для хранения текста результата
result_text = tk.StringVar(value="Жду вашего хода...")

# Заголовок
label_1 = tk.Label(win, text="Числовая угадайка!",
                   bg="#c2c2c2",
                   fg="#4d4a4a",
                   font=('Arial', 20, "bold"),
                   padx=40,
                   pady=40)
label_1.pack()

# Метка для отображения результата из функции
label_result = tk.Label(win,
                       textvariable=result_text,
                       bg="#c2c2c2",
                       fg="#4d4a4a",
                       font=('Arial', 14),
                       wraplength=400)  # перенос текста
label_result.pack(pady=20)

# Кнопка
button = tk.Button(win, text='Старт', command=f.button_click)
button.pack(pady=10)

win.mainloop()