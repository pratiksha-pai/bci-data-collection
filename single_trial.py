from Custom_Packages import gloves
from Custom_Packages import eeg
import multiprocessing
import os
from datetime import datetime
from sensorimotorkit.acquire_images.main import main

def get_save_path():
    base_path = "C:/Users/Data acquisition/bci-data-collection/Data/Single Trials"
    today_str = datetime.now().strftime('%Y-%m-%d')
    folder_path = os.path.join(base_path, today_str)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    todays_trials = os.listdir(folder_path)
    trial_number = len(todays_trials)
    trial_path = os.path.join(folder_path, str(trial_number))
    os.makedirs(trial_path)
    return trial_path


def start_bodycam(save_path):
    print("collecting bodycam data")
    main(duration=10)

def start_gloves(save_path):
    print("collecting gloves data")
    gloves.collect(10, save_path)

def start_eeg(save_path):
    print("collecting eeg")
    eeg.collect(10, save_path)

def capture_board(save_path):
    print("capturing board")

def run_trial():
    save_path = get_save_path()

    proc_bodycam = multiprocessing.Process(target=start_bodycam, args=(save_path,))
    proc_gloves = multiprocessing.Process(target=start_gloves, args=(save_path,))
    proc_eeg = multiprocessing.Process(target=start_eeg, args=(save_path,))
    
    proc_bodycam.start()
    proc_gloves.start()
    proc_eeg.start()

    proc_bodycam.join()
    proc_gloves.join()
    proc_eeg.join()


    proc_bodycam.terminate()
    proc_gloves.terminate()
    proc_eeg.terminate()

    capture_board(save_path)

if __name__ == '__main__':
    run_trial()
