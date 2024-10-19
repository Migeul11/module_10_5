from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


# Линейный вызов
if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start = datetime.now()
    for filename in filenames:
        read_info(filename)
    stop = datetime.now()
    print(f"{stop-start} (линейный)")

    # Многопроцессный
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    stop = datetime.now()
    print(f"{stop-start} (многопроцессный)")
