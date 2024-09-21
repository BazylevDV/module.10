import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


# Взятие текущего времени перед выполнением функций
start_time_functions = time.time()

# Запуск функций с аргументами из задачи
write_words(10, 'example_1.txt')
write_words(30, 'example_2.txt')
write_words(200, 'example_3.txt')
write_words(100, 'example_4.txt')

# Взятие текущего времени после выполнения функций
end_time_functions = time.time()

# Вывод разницы начала и конца работы функций
print(f"Работа потоков: {end_time_functions - start_time_functions:.6f} секунд")

# Взятие текущего времени перед запуском потоков
start_time_threads = time.time()

# Создание и запуск потоков с аргументами из задачи
threads = []
for word_count, file_name in [(10, 'example_5.txt'), (30, 'example_6.txt'),
                              (200, 'example_7.txt'), (100, 'example_8.txt')]:
    thread = Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

# Взятие текущего времени после завершения потоков
end_time_threads = time.time()

# Вывод разницы начала и конца работы потоков
print(f"Работа потоков: {end_time_threads - start_time_threads:.6f} секунд")