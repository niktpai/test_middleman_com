import serial
import time

UART_PORT = '/dev/ttyVirtual0' 
PC_PORT = '/dev/ttyVirtual1'  
BAUD_RATE = 9600

def setup_serial(port):
    return serial.Serial(port, BAUD_RATE, timeout=0.1)

def monitor_communication():
    uart_ser = setup_serial(UART_PORT)
    pc_ser = setup_serial(PC_PORT)

    print("Starting communication monitor on Pi 1...")

    try:
        while True:
            # Check for data from PC software
            if pc_ser.in_waiting:
                data = pc_ser.readline().decode('utf-8').strip()
                print(f"PC -> Pi 2: {data}")
                uart_ser.write(data.encode('utf-8') + b'\n')

            # Check for data from Pi 2 (via UART)
            if uart_ser.in_waiting:
                data = uart_ser.readline().decode('utf-8').strip()
                print(f"Pi 2 -> PC: {data}")
                pc_ser.write(data.encode('utf-8') + b'\n')

            time.sleep(0.01)  # Small delay to prevent CPU overuse

    except KeyboardInterrupt:
        print("Monitoring stopped.")
    finally:
        uart_ser.close()
        pc_ser.close()

if __name__ == "__main__":
    monitor_communication()