# Gesture Volume Control  

A Python project that allows you to control your system's volume using hand gestures via your webcam.  

## Features  
- Adjust system volume with hand gestures.  
- Real-time hand tracking.  
- Simple and touch-free interaction.  

## Libraries Used  
- **OpenCV (cv2)**: For webcam access and image processing.  
- **Mediapipe**: For hand detection and tracking.  
- **PyAutoGUI**: To control system volume.  

## How It Works  
1. The webcam captures the video feed.  
2. Mediapipe detects and tracks your hand landmarks in real time.  
3. The distance between specific landmarks (e.g., thumb and index finger) determines the volume level.  
4. PyAutoGUI adjusts the system volume accordingly.  

# Install the required libraries:
pip install opencv-python mediapipe pyautogui  

# Run the script:
1. python gesture_volume_control.py
2. Make a gesture (e.g., move your thumb and index finger closer or farther) to adjust the volume.


# Contributing

Feel free to fork this repository, submit issues, or create pull requests to contribute!

