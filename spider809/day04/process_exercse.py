import random
import multiprocessing
import time


def compute(i):
    return sum([random.randint(1, 100) for i in range(1000000)])


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=8)
    t1 = time.time()
    print(pool.map(compute, range(8)))
    t2 = time.time()
    print(t2-t1)
