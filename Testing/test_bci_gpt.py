import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams

# Setup parameters for your board
params = BrainFlowInputParams()
# If required for your board, set additional parameters e.g., serial port for Cyton:
params.serial_port = '/dev/cu.usbserial-D200QRN6'

# Initialize board
board_id = brainflow.BoardIds.CYTON_BOARD.value  # Replace this with the appropriate board ID
board = BoardShim(board_id, params)

# Prepare and start the board
board.prepare_session()
board.start_stream()

# Collect data for a certain time
import time
time.sleep(10)  # Collect data for 10 seconds

# Stop the board and get the data
board.stop_stream()
data = board.get_board_data()  # This will retrieve the recent data
print(data.shape)
board.release_session()

# Now, `data` contains the recorded EEG data. You can process or save it as needed.
