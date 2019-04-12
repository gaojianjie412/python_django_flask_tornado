import random
import threading


result = []


def compute():
    result.append(sum([random.randint(1, 100) for i in range(1000000)]))


threads = [threading.Thread(target=compute) for i in range(8)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(result)