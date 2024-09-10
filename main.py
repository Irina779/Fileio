from tkinter import *
import requests # requests- это запросы, которые будем делать  к сайту file.io
from tkinter import filedialog as fd
from tkinter import ttk# используем виджеты ttk

def upload():# создаем функцию upload
    filepath = fd.askopenfilename()# сначало пулучим путь к файлу, который
    # будем загружать (filepath-путь к файлу), получим при помощи
    # фаилдиалога fd.askopenfilename()
    if filepath:# если переменная не пустая и нам удалось ее создать и положить
        # в нее путь к файлу то мы можем это проверить.
        # Переменная не пустая значит открываем то что внутри if
        files = {'file': open(filepath, 'rb')}# открываем фаил в режиме для чтения по байтно
        response = requests.post('https://file.io', files=files)# response-ответ,
        # который мы получим когда отправим запрос, вид запроса post, указываем путь (https://file.io),
        # указываем какой фаил отправляем (files=files)
        if response.status_code == 200: # делаем проверку, получаем ответ от сайта file.io,
            # если все хорошо то ответ равен 200 link
            link = response.json()['link'] # и мы можем положить в ссылку link положить то что
            # нам прислали из ответа.   response.json() потому что ответ в формате json и
            # выбираем параметр link, чтобы выбрать параметр надо указать в квадратных скобках ключ
            # и тогда ссылка сама прилетит в переменную link и мы сможем ее вывести в поле ввода

            entry.insert(0, link)# с начальной поцизии 0 вставляем ссылку

window = Tk()# создаем окно
window.title("Сохранение файлов в облаке")# заголовок
window.geometry('400x200') # размер окна

upload_button = ttk.Button(text="Загрузить файл", command=upload)
upload_button.pack()# создаем и размещаем кнопку, command=upload (загрузка)

entry = ttk.Entry()# поле в которое будет выведена ссылка на наш загруженный фаил,
# чтобы ее потом можно было выделить и скопировать
entry.pack()

window.mainloop()

