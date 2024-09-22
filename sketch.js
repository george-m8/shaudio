let low = 0, mid = 0, high = 0;  // Initialize with default values
let socket;

function setup() {
  createCanvas(854, 480); // 480p size (854x480)
  frameRate(30); // Run at 30 FPS

  // Establish WebSocket connection
  socket = new WebSocket('ws://localhost:6789');

  // Log when connection opens
  socket.onopen = function() {
    console.log("WebSocket connection opened");
  };

  // Log incoming messages
  socket.onmessage = function(event) {
    console.log("Data received:", event.data);  // Log raw data
    let data = JSON.parse(event.data);

    // Check if data contains low, mid, high and assign them
    if (data.low !== undefined && data.mid !== undefined && data.high !== undefined) {
      low = data.low * 100;
      mid = data.mid * 100;
      high = data.high * 100;
      console.log("Low:", low, "Mid:", mid, "High:", high);
    } else {
      console.error("Received data is missing low, mid, or high:", data);
    }
  };

  // Log any WebSocket errors
  socket.onerror = function(error) {
    console.error("WebSocket Error:", error);
  };

  // Log when WebSocket closes
  socket.onclose = function() {
    console.log("WebSocket connection closed");
  };
}

function draw() {
  background(0); // Set the background to black

  // Ensure values are defined before mapping
  fill(0, 255, 0); // Green for low frequencies
  rect(100, height, 100, -map(low || 0, 0, 100, 0, height)); // Use default 0 if undefined

  fill(255, 255, 0); // Yellow for mid frequencies
  rect(300, height, 100, -map(mid || 0, 0, 100, 0, height)); // Use default 0 if undefined

  fill(255, 0, 0); // Red for high frequencies
  rect(500, height, 100, -map(high || 0, 0, 100, 0, height)); // Use default 0 if undefined
}
