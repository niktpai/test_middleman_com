import serial

# Set up the serial connection
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

try:
    while True:
        # Read incoming message
        incoming = ser.readline().decode('utf-8').strip()
        if incoming:
            print(f"Received: {incoming}")
            
            # Send a response
            response = "Message received by Raspberry Pi 2!"
            ser.write(response.encode('utf-8'))
            print(f"Sent: {response}")

except KeyboardInterrupt:
    print("Receiver script terminated.")
finally:
    ser.close()