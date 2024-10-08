"""
Задание №9
� Написать программу, которая скачивает изображения с заданных URL-адресов и
сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
� Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
image1.jpg
� Программа должна использовать многопоточный, многопроцессорный и
асинхронный подходы.
� Программа должна иметь возможность задавать список URL-адресов через
аргументы командной строки.
� Программа должна выводить в консоль информацию о времени скачивания
каждого изображения и общем времени выполнения программы.
"""

import requests
import time
import os


# Функция для скачивания изображения по заданному URL адресу
def download_image(url: str):
    start_time = time.time()
    filename = url.split("/")[-1]
    img_data = requests.get(url)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    with open(os.path.join(os.getcwd(), "downloads", filename), "wb") as image:
        image.write(img_data.content)
        print(f"Время скачивания картинки: {time.time() - start_time:.2f} секунд")


if __name__ == "__main__":
    download_image(
        "https://cdn.fishki.net/upload/post/2021/01/23/3568147/f09ed522033c8c029693c5c28592a76f.jpg"
    )