from Custom_Packages import gloves
from Custom_Packages import eeg
import multiprocessing
from sensorimotorkit.acquire_images.main import main

def start_bodycam():
    print("collecting bodycam data")
    main(duration=10)

def start_gloves():
    print("collecting gloves data")
    gloves.collect(10)

def start_eeg():
    print("collecting eeg")
    eeg.collect_eeg(10)

def capture_board():
    print("capturing board")

def run_trial():
    proc_bodycam = multiprocessing.Process(target=start_bodycam)
    proc_gloves = multiprocessing.Process(target=start_gloves)
    proc_eeg = multiprocessing.Process(target=start_eeg)
    
    proc_bodycam.start()
    proc_gloves.start()
    proc_eeg.start()

    proc_bodycam.join()
    proc_gloves.join()
    proc_eeg.join()

    proc_bodycam.terminate()
    proc_gloves.terminate()
    proc_eeg.terminate()

    capture_board()

if __name__ == '__main__':
    run_trial()