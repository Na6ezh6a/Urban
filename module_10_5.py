# Задача "Многопроцессное считывание".
from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break

if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.now()
    for file_name in filenames:
        read_info(file_name)
        end_time = datetime.now()
        linear_duration = end_time - start_time
        print(f"Время линейного чтения: {linear_duration}")

    start_time = datetime.now()
    with Pool() as pool:
        all_data = pool.map(read_info, filenames)
    end_time = datetime.now()
    multiprocessing_duration = end_time - start_time
    print(f"Время многопроцессорного чтения: {multiprocessing_duration}")
