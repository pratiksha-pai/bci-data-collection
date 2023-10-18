import time
import threading
import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams

def collect_eeg_data(serial_port, duration_in_seconds=5):
    params = BrainFlowInputParams()
    params.serial_port = serial_port
    
    board_id = 2  # OpenBCI Cyton over Bluetooth
    
    board = BoardShim(board_id, params)
    board.prepare_session()
    board.start_stream()

    time.sleep(duration_in_seconds)

    data = board.get_board_data()

    board.stop_stream()
    board.release_session()

    return data

def thread_function(serial_port):
    print(f"Starting thread for {serial_port}")
    eeg_data = collect_eeg_data(serial_port)
    print(f"Data from {serial_port}:")
    print(eeg_data)

if __name__ == "__main__":
    # Assume your two EEG devices are on 'COM3' and 'COM4'
    t1 = threading.Thread(target=thread_function, args=('COM3',))
    t2 = threading.Thread(target=thread_function, args=('COM4',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
