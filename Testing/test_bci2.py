import time
import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.exit_codes import BrainFlowExitCodes

def collect_eeg_data(duration_in_seconds=5):
    params = BrainFlowInputParams()
    params.serial_port = 'COM3'
    
    board_id = 2  # OpenBCI Cyton over Bluetooth
    
    try:
        board = BoardShim(board_id, params)
        board.prepare_session()
        board.start_stream()

        # Collect data for the specified duration
        time.sleep(duration_in_seconds)

        # Retrieve the data
        data = board.get_board_data()

        # Stop the data stream and release the session
        board.stop_stream()
        board.release_session()

        return data

    except brainflow.exit_codes.BrainFlowError as e:
        # Error handling for BrainFlow specific errors
        if e.exit_code == BrainFlowExitCodes.BOARD_NOT_CREATED_ERROR:
            print("Error: Board not created. Ensure the device is connected and try again.")
        elif e.exit_code == BrainFlowExitCodes.STATUS_OK_ERROR:  # The board is already initialized
            print("Board is already initialized.")
        else:
            print(f"BrainFlowError encountered: {e}")
        return None

    except Exception as e:
        # General error handling
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    eeg_data = collect_eeg_data()
    if eeg_data is not None:
        print(eeg_data)
