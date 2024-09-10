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


window = Tk()# создаем окно
window.title("Сохранение файлов в облаке")# заголовок
window.geometry('400x200') # размер окна

upload_button = ttk.Button(text="Загрузить файл", command=upload)
upload_button.pack()# создаем и размещаем кнопку, command=upload (загрузка)

entry = ttk.Entry()# поле в которое будет выведена ссылка на наш загруженный фаил,
# чтобы ее потом можно было выделить и скопировать
entry.pack()

window.mainloop()

