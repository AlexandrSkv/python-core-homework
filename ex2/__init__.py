from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов
    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        # put your code here
        def wrap(url):
            all_time = 0
            for i in range(num):
                start = time.time()
                func(url)
                end = time.time()
                print (f'execution time: {end - start}')
                all_time += end - start
            print (f'average execution time: {all_time/num}')
        return wrap
        
    return wrapper

@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
