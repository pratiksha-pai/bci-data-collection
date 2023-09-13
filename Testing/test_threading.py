import multiprocessing
import time

def print_numbers():
    last_time = time.time()
    for i in range(1, 6):
        print(f"Number: {i}")
        current_time = time.time()
        elapsed_time = current_time - last_time
        print("num: " + str(elapsed_time))
        last_time = current_time
        time.sleep(0.001)

def print_letters():
    last_time = time.time()
    for letter in 'abcdefgh':
        print(f"Letter: {letter}")
        current_time = time.time()
        elapsed_time = current_time - last_time
        print("let: " + str(elapsed_time))
        last_time = current_time
        time.sleep(0.0001)

if __name__ == '__main__':
    # Create processes
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)

    # Start processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    print("Both processes have finished.")
