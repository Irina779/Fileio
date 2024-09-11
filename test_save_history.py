
# json тест для проверки функции save_history
import json
import os

history_file = "test_save_history.json"# тестовый фаил test_save_history

def save_history(file_path, link):# функция, которую тестируем
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
    history.append({"file_path": os.path.basename(file_path), "download_link": link})
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)

def test_save_history():# создаем тестовую функцию, которая будет ее запускать и проверять
    test_file_path = "test_file.txt"# тестовый путь, test_file_path (тестовая переменная),
    # как будто выбрали на компе фаил и загрузили
    test_download_link = "https://file.io/kjdfvfdkhj"# как будто сайт  file.io вернет строку kjdfvfdkhj
    # (kjdfvfdkhj - просто набор символов взятый для примера)

    # Вызов функции для тестирования
    save_history(test_file_path, test_download_link)

    # Проверка, что история была сохранена корректно
    with open("test_save_history.json", "r") as f:# смотрим что внутри, читаем, будет известен как f
        history = json.load(f)# в переменную history загрузим с помощь json load содержимое файла f
        assert len(history) == 1 # проверяем длинну
        assert history[0]['file_path'] == test_file_path # проверяем конкретное значение
        assert history[0]['download_link'] == test_download_link # download_link- ключ

    # Очистка тестовых данных
    os.remove("test_upload_history.json") # удаляем этот фаил

# Вызов функции тестирования
test_save_history()
