import multiprocessing
import time

def process_1():
    last_time = time.time()
    sum = 0
    count = 0
    for i in range(1, 100):
        current_time = time.time()
        elapsed_time = current_time - last_time
        count = count + 1
        sum = sum + elapsed_time
        last_time = current_time
        time.sleep(0.001)
    avg = sum / count
    print("1: " + str(avg))

def process_2():
    last_time = time.time()
    sum = 0
    count = 0
    for i in range(1, 10000):
        current_time = time.time()
        elapsed_time = current_time - last_time
        count = count + 1
        sum = sum + elapsed_time
        last_time = current_time
        time.sleep(0.0001)
    avg = sum / count
    print("2: " + str(avg))

def process_3():
    last_time = time.time()
    sum = 0
    count = 0
    for i in range(1, 300):
        current_time = time.time()
        elapsed_time = current_time - last_time
        count = count + 1
        sum = sum + elapsed_time
        last_time = current_time
        time.sleep(0.00001)
    avg = sum / count
    print("3: " + str(avg))


if __name__ == '__main__':
    # Create processes
    process1 = multiprocessing.Process(target=process_1)
    process2 = multiprocessing.Process(target=process_2)
    process3 = multiprocessing.Process(target=process_3)

    # Start processes
    process1.start()
    process2.start()
    process3.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()
    process3.join()
