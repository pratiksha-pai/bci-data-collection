import serial
import psutil

port_name = 'COM4' 

def check_serial_port(port):
    ser = serial.Serial()
    ser.port = port
    try:
        ser.open()
        ser.close()
        print(f'{port} is available')
    except serial.SerialException as e:
        print(f'{port} is not available: {str(e)}')

def find_occupying_process(port):
    for proc in psutil.process_iter(['pid', 'connections']):
        for conn in proc.connections():
            if conn.laddr.port == port:
                return proc
    return None

check_serial_port(port_name)

# Assuming COM ports correspond to the same numerical value as TCP/UDP ports,
# which may not always be the case.
# The conversion from COM port to numerical port value might need adjustment.
numerical_port_value = int(port_name.replace('COM', ''))  
occupying_process = find_occupying_process(numerical_port_value)

if occupying_process:
    print(f'Port {port_name} is occupied by process ID: {occupying_process.info["pid"]}')
else:
    print(f'No process found occupying {port_name}')
