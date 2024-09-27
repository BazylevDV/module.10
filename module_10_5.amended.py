import os
import time
from multiprocessing import Pool


def read_info(name):
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
        
        


def linear_read(filenames):
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейное время выполнения: {end_time - start_time} секунд")


def multiprocess_read(filenames):
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессное время выполнения: {end_time - start_time} секунд")


if __name__ == "__main__":

    filenames = [
        'C:/Users/bdv/PycharmProjects/pythonProject36/file 1.txt',
        'C:/Users/bdv/PycharmProjects/pythonProject36/file 2.txt',
        'C:/Users/bdv/PycharmProjects/pythonProject36/file 3.txt',
        'C:/Users/bdv/PycharmProjects/pythonProject36/file 4.txt'
    ]

    # Проверка существования файлов
    for filename in filenames:
        if not os.path.exists(filename):
            print(f"Файл {filename} не найден.")
            exit(1)

    # Линейный вызов
    linear_read(filenames)

    # Многопроцессный вызов
    multiprocess_read(filenames)
