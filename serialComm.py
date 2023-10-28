import serial
import time
from hand_tracking import get_hand_positions

# Initialize serial connection
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to your Arduino's port
time.sleep(2)

def send_data_to_arduino(data):
    # Logic to send data to Arduino
    ser.write(data.encode())

# Main loop for sending data
if __name__ == "__main__":
    while True:
        data = get_hand_positions()
        send_data_to_arduino(data)
        time.sleep(0.1)
