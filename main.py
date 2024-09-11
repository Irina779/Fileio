from tkinter import *
import requests # requests- это запросы, которые будем делать  к сайту file.io
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import pyperclip # добавляем библиотеку
from tkinter import ttk# используем виджеты ttk
import json # добавляем библиотеку
import os # добавляем операционную сисстему

history_file = "upload_history.json"# добавляем переменную, текстовый фаил в формате json

def save_history(file_path, link):#создаем функцию save_history
    #путь к файлу (file_path), ссылка (link)
    history = []# изначально переменная history это пустой список
    if os.path.exists(history_file):# проверяем что history_file существует в нашей папке
        with open(history_file, "r") as f:# тогда его открываем для чтения
            history = json.load(f)# загружаем то что уже есть в фаиле, если пустой ничего не загрузим
            # но если что-то было то в переменную history загрузим новую информацию и при помощи append
            # добавим новую информацию. Перед тем кам дополнить надо проверить старый.


    # добавляем новую информацию в историю словарь(в круглых скобках), ключ file_path
    # получим при помощи os.path.basename, download_link (по этой ссылке находится
    history.append({"file_path": os.path.basename(file_path), "download_link": link})

    with open(history_file, "w") as file:# открываем фаил для записи ("w")
        json.dump(history, file, indent=4)# 4 отступа


def upload():# создаем функцию upload
    try:
        filepath = fd.askopenfilename()# сначало пулучим путь к файлу, который
        # будем загружать (filepath-путь к файлу), получим при помощи
        # фаилдиалога fd.askopenfilename()
        if filepath:# если переменная не пустая и нам удалось ее создать и положить
            # в нее путь к файлу то мы можем это проверить.
            # Переменная не пустая значит открываем то что внутри if
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://file.io', files=files)
                response.raise_for_status()
                link = response.json()['link'] # и мы можем положить в ссылку link положить то что
                    # нам прислали из ответа.   response.json() потому что ответ в формате json и
                    # выбираем параметр link, чтобы выбрать параметр надо указать в квадратных скобках ключ
                    # и тогда ссылка сама прилетит в переменную link и мы сможем ее вывести в поле ввода
                entry.delete(0,END)
                entry.insert(0, link)# с начальной поцизии 0 вставляем ссылку
                pyperclip.copy(link)  # Копирование ссылки в буфер обмена
                save_history(filepath, link)
                mb.showinfo("Ссылка скопирована", f"Ссылка {link}успешно скопирована в буфер обмена")

    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


def show_history(): # создаем функцию
    if not os.path.exists(history_file):# делаем проверку есть ли фаил
        messagebox.showinfo("История", "История загрузок пуста") # если файла не существуем
        return

    history_window = Toplevel(window)# создаем еще одно окно
    history_window.title("История Загрузок") # заголовок

    # files_listbox -список файлов
    files_listbox = Listbox(history_window, width=50, height=20)# создаем первый лист бокс, находится в
    # history_window, ширина 50, высота 20
    files_listbox.grid(row=0, column=0, padx=(10,0), pady=10)# размещаем по сетке при помощи grid
    # строка 0, колонка 0, ( padx=(10,0) отступ слева 10, право 0), отступ по y=10 (отступы сверху и снизу)

    # links_listbox -список ссылок
    links_listbox = Listbox(history_window, width=50, height=20)# второй listbox
    links_listbox.grid(row=0, column=1, padx=(0,10) вплотную и рамочка 10, pady=10)# строка 0, колонка 1

    with open(history_file, "r") as f:# открыавем фаил и раскладываем по спискам для чтения
        history = json.load(f)# положим то что загрузим из джейсон
        for item in history:# создаем цикл history-это список словарей, надо все перебрать
            files_listbox.insert(END, item['file_path'])# вставляем в конец списка
            # выбираем по ключу, ключ file_path берем из upload_history.json
            links_listbox.insert(END, item['download_link'])



window = Tk()# создаем окно
window.title("Сохранение файлов в облаке")# заголовок
window.geometry('400x200') # размер окна

upload_button = ttk.Button(text="Загрузить файл", command=upload)
upload_button.pack()# создаем и размещаем кнопку, command=upload (загрузка)

entry = ttk.Entry()# поле в которое будет выведена ссылка на наш загруженный фаил,
# чтобы ее потом можно было выделить и скопировать
entry.pack()

history_button = ttk.Button(text="Показать Историю", command=show_history)
history_button.pack()


window.mainloop()

