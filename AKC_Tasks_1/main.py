import requests
import threading
import concurrent.futures
import multiprocessing
import re
from collections import Counter

#Функция, которая параллельно загружает несколько изображений с удаленного сервера и сохраняет их на локальном диске.
def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
            print(f"Изображение {file_name} успешно загружено.")

# Список URL-адресов изображений для загрузки
image_urls = [
    'https://example.com/image1.jpg',
    'https://example.com/image2.jpg',
    'https://example.com/image3.jpg',
    # Добавьте дополнительные URL-адреса изображений, если необходимо
]

# Создаем список для хранения потоков выполнения
threads = []

# Запускаем параллельную загрузку изображений
for i, url in enumerate(image_urls):
    file_name = f"image{i+1}.jpg"  # Имя файла для сохранения
    thread = threading.Thread(target=download_image, args=(url, file_name))
    thread.start()
    threads.append(thread)

# Ждем, пока все потоки выполнения завершатся
for thread in threads:
    thread.join()

print("Завершение программы")

#'В этом примере мы используем модуль requests для выполнения HTTP-запросов и скачивания изображений.
# Функция download_image принимает URL-адрес изображения и имя файла, в который будет сохранено изображение.
# Внутри функции мы отправляем GET-запрос по указанному URL-адресу, проверяем успешность запроса, а затем сохраняем содержимое ответа в файл.
# Мы создаем список image_urls, в котором содержатся URL-адреса изображений для загрузки. Затем мы создаем список threads для хранения потоков выполнения.
# В цикле for мы перебираем URL-адреса изображений и создаем для каждого URL-адреса отдельный поток выполнения. Внутри потока вызывается функция download_image с передачей URL-адреса и имени файла.
# После создания потока мы запускаем его методом start и добавляем в список threads.Затем мы ожидаем, пока все потоки выполнения завершатся, используя метод join для каждого потока из списка threads.
# Наконец, выводится сообщение 'Завершение программы'.



#Программа, которая создает два отдельных потока выполнения и параллельно считывает и выводит содержимое двух разных файлов.
def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        print(f"Содержимое файла {file_name}:")
        print(content)

# Создаем два потока выполнения
thread1 = threading.Thread(target=read_file, args=('file1.txt',))
thread2 = threading.Thread(target=read_file, args=('file2.txt',))

# Запускаем потоки выполнения
thread1.start()
thread2.start()

# Ждем, пока оба потока завершатся
thread1.join()
thread2.join()

print("Завершение программы")


#В этом примере мы создаем две функции read_file, которые считывают и выводят содержимое файлов.
# Затем мы создаем два объекта Thread, указывая функцию read_file и имя файла в качестве аргументов.
# После этого мы запускаем потоки выполнения методом start и ждем, пока они завершатся с помощью метода join.
# Наконец, выводится сообщение "Завершение программы".


#Функция, которая параллельно загружает несколько изображений с удаленного сервера и сохраняет их на локальном диске.
def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
            print(f"Изображение {file_name} успешно загружено.")

# Список URL-адресов изображений для загрузки
image_urls = [
    'https://example.com/image1.jpg',
    'https://example.com/image2.jpg',
    'https://example.com/image3.jpg',
    # Добавьте дополнительные URL-адреса изображений, если необходимо
]

# Создаем список для хранения потоков выполнения
threads = []

# Запускаем параллельную загрузку изображений
for i, url in enumerate(image_urls):
    file_name = f"image{i+1}.jpg"  # Имя файла для сохранения
    thread = threading.Thread(target=download_image, args=(url, file_name))
    thread.start()
    threads.append(thread)

# Ждем, пока все потоки выполнения завершатся
for thread in threads:
    thread.join()

print("Завершение программы")

#В этом примере мы используем модуль requests для выполнения HTTP-запросов и скачивания изображений. Функция download_image принимает URL-адрес изображения и имя файла, в который будет сохранено изображение.
# Внутри функции мы отправляем GET-запрос по указанному URL-адресу, проверяем успешность запроса, а затем сохраняем содержимое ответа в файл.Мы создаем список image_urls, в котором содержатся URL-адреса изображений для загрузки.
# Затем мы создаем список threads для хранения потоков выполнения.В цикле for мы перебираем URL-адреса изображений и создаем для каждого URL-адреса отдельный поток выполнения. Внутри потока вызывается функция download_image с передачей URL-адреса и имени файла.
# После создания потока мы запускаем его методом start и добавляем в список threads.Затем мы ожидаем, пока все потоки выполнения завершатся, используя метод join для каждого потока из списка threads.
# Наконец, выводится сообщение "Завершение программы".



#программа, которая параллельно сортирует большой список целых чисел, используя алгоритм быстрой сортировки.
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    smaller, equal, larger = [], [], []
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    return quicksort(smaller) + equal + quicksort(larger)

def parallel_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    smaller, equal, larger = [], [], []
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    smaller_thread = threading.Thread(target=lambda: parallel_quicksort(smaller))
    larger_thread = threading.Thread(target=lambda: parallel_quicksort(larger))

    smaller_thread.start()
    larger_thread.start()

    smaller_thread.join()
    larger_thread.join()

    return quicksort(smaller) + equal + quicksort(larger)

# Создаем большой список целых чисел для сортировки
numbers = [5, 2, 9, 1, 7, 6, 3, 8, 4, 10]  # Замените данный список своими данными

# Вызываем параллельную сортировку
sorted_numbers = parallel_quicksort(numbers)

# Выводим отсортированный список
print("Отсортированный список:")
print(sorted_numbers)

#В этом примере используется алгоритм быстрой сортировки для сортировки списка целых чисел. Функция quicksort рекурсивно разделяет список на три подсписка: меньшие числа, равные числа и большие числа, а затем объединяет их в правильном порядке.
# Функция parallel_quicksort работает аналогично, но дополнительно создает два потока выполнения для сортировки меньших и больших подсписков. Затем она запускает потоки выполнения, ждет их завершения и объединяет результаты.
# В приведенном примере список чисел [5, 2, 9, 1, 7, 6, 3, 8, 4, 10] используется для сортировки. Можно заменить этот список на свой собственный.


# скрипт, который параллельно отправляет HTTP-запросы на несколько веб-сайтов и выводит статус коды ответов
def check_website(url):
    response = requests.get(url)
    print(f"Статус код для {url}: {response.status_code}")

# Список URL-адресов веб-сайтов для проверки
websites = [
    'https://example.com',
    'https://google.com',
    'https://github.com',
    # Добавьте дополнительные URL-адреса веб-сайтов, если необходимо
]

# Создаем пул потоков выполнения
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Запускаем параллельные HTTP-запросы
    futures = [executor.submit(check_website, url) for url in websites]

    # Ожидаем завершения всех запросов
    concurrent.futures.wait(futures)

print("Завершение программы")

#В этом примере мы используем модуль concurrent.futures для создания пула потоков выполнения. Функция check_website выполняет HTTP-запрос по заданному URL-адресу и выводит статус-код ответа.Мы создаем список websites, в котором указаны URL-адреса веб-сайтов для проверки.
# Затем мы создаем пул потоков выполнения с помощью ThreadPoolExecutor. В цикле for мы отправляем каждый URL-адрес веб-сайта в функцию check_website с использованием метода submit, который возвращает объект Future для каждого запроса.После этого мы вызываем concurrent.futures.wait для ожидания завершения всех запросов.
# Наконец, выводится сообщение "Завершение программы".


#программa, которая параллельно выполняет вычисления сложных математических формул на нескольких ядрах процессора.
def calculate_formula(formula):
    result = eval(formula)
    print(f"Результат формулы '{formula}': {result}")

# Список сложных математических формул для вычисления
formulas = [
    "2 + 3 * 4 / 2 - 1",
    "sqrt(16)",
    "log10(100)",
    # Добавьте дополнительные формулы для вычисления, если необходимо
]

# Создаем пул процессов
with multiprocessing.Pool() as pool:
    # Выполняем параллельные вычисления
    pool.map(calculate_formula, formulas)

print("Завершение программы")
#В этом примере мы используем модуль multiprocessing для создания пула процессов. Функция calculate_formula принимает сложную математическую формулу, вычисляет ее с помощью функции eval и выводит результат.
# Мы создаем список formulas, в котором содержатся сложные математические формулы для вычисления.Затем мы создаем пул процессов с помощью Pool. Внутри контекста пула процессов мы используем метод map, чтобы параллельно применить функцию calculate_formula ко всем формулам в списке formulas.
# Результаты будут автоматически собраны и возвращены в том же порядке.Наконец, выводится сообщение "Завершение программы".

#функция, которая параллельно обрабатывает большой объем текстовых данных, разбивая его на отдельные слова и подсчитывая частоту встречаемости каждого слова.
def process_text(text):
    # Разбиваем текст на отдельные слова с помощью регулярного выражения
    words = re.findall(r'\w+', text.lower())

    # Подсчитываем частоту встречаемости каждого слова
    word_counts = Counter(words)

    return word_counts

def parallel_text_processing(text):
    # Разбиваем текст на части для обработки параллельно
    num_processes = multiprocessing.cpu_count()
    chunk_size = len(text) // num_processes
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Создаем пул процессов
    with multiprocessing.Pool() as pool:
        # Обрабатываем каждую часть текста параллельно
        results = pool.map(process_text, chunks)

    # Объединяем результаты подсчета частоты слов
    final_word_counts = Counter()
    for result in results:
        final_word_counts += result

    return final_word_counts

# Пример использования
text = """
Python is a high-level programming language designed to be easy to read and simple to implement.
It is open source, which means it is free to use, even for commercial purposes.
Python can run on Mac, Windows, and Unix systems and has also been ported to Java and .NET virtual machines.
Python is widely used in web development, scientific computing, artificial intelligence, data analysis, and more.
"""

word_counts = parallel_text_processing(text)
print("Частота встречаемости слов:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

#В этом примере функция process_text принимает текст и разбивает его на отдельные слова с помощью регулярного выражения. Затем она подсчитывает частоту встречаемости каждого слова с использованием Counter.
# Функция parallel_text_processing разбивает текст на части для параллельной обработки. Она создает пул процессов с помощью Pool и использует метод map, чтобы обработать каждую часть текста параллельно с помощью функции process_text. Результаты обработки объединяются в конечный объект Counter.
# Пример использования показывает, как передать текст в функцию parallel_text_processing и получить частоту встречаемости каждого слова. Результаты выводятся на экран.






