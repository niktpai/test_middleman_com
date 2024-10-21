
import serial
import time

# Set up the serial connection
ser = serial.Serial('/dev/pts/2', 9600, timeout=1)

try:
    while True:
        # Send a message
        message = "Hello from Raspberry Pi 1!"
        ser.write(message.encode('utf-8'))
        print(f"Sent: {message}")
        
        # Wait for a response
        response = ser.readline().decode('utf-8').strip()
        if response:
            print(f"Received: {response}")
        
        time.sleep(2)  # Wait for 2 seconds before sending the next message

except KeyboardInterrupt:
    print("Sender script terminated.")
finally:
    ser.close()