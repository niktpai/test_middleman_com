import serial
import time

UART_PORT = '/dev/ttyACM0'
PC_PORT = '/dev/pts/2'
BAUD_RATE = 9600

def setup_serial(port):
    return serial.Serial(port, BAUD_RATE, timeout=0.1)

def replace_message(source):
    return f"This message is from the middle man (original source: {source})"

def monitor_and_replace():
    uart_ser = setup_serial(UART_PORT)
    pc_ser = setup_serial(PC_PORT)

    print("Starting message replacing monitor on Pi 1...")

    try:
        while True:
            # Check for data from PC software
            if pc_ser.in_waiting:
                original_data = pc_ser.readline().decode('utf-8').strip()
                print(f"Original PC -> Pi 2: {original_data}")
                new_message = replace_message("PC")
                print(f"Replaced message: {new_message}")
                uart_ser.write(new_message.encode('utf-8') + b'\n')

            # Check for data from Pi 2 (via UART)
            if uart_ser.in_waiting:
                original_data = uart_ser.readline().decode('utf-8').strip()
                print(f"Original Pi 2 -> PC: {original_data}")
                new_message = replace_message("Pi 2")
                print(f"Replaced message: {new_message}")
                pc_ser.write(new_message.encode('utf-8') + b'\n')

            time.sleep(0.01)  # Small delay to prevent CPU overuse

    except KeyboardInterrupt:
        print("Message replacing monitor stopped.")
    finally:
        uart_ser.close()
        pc_ser.close()

if __name__ == "__main__":
    monitor_and_replace()