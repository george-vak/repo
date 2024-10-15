import timeit

def time():
    sip = input()
    timer = timeit.Timer(sip)
    nums, tim = timer.autorange()
    print(f"Среднее время на запуск: {tim / nums}")

time()
