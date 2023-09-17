import time
import multiprocessing
import datetime

elapsed = 0
last_time = time.time()

while True:
    current_time = time.time()
    step_time = current_time - last_time
    elapsed = elapsed + step_time
    last_time = current_time
    print(elapsed)

    pause(1)
    