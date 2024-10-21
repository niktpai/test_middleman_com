void setup() {
  // Initialize serial communication
  Serial.begin(9600);  // Use the same baud rate as the Raspberry Pi
  while (!Serial) {
    ; // Wait for serial port to connect. Needed for native USB port only
  }
  Serial.println("Arduino Due ready for communication!");
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    // Read the incoming data
    String incomingMessage = Serial.readStringUntil('\n');
    
    // Print the received message
    Serial.print("Received: ");
    Serial.println(incomingMessage);
    
    // Send a response
    String response = "Hello from Arduino Due!";
    Serial.println(response);
  }
  
  // Small delay to prevent excessive looping
  delay(10);
}