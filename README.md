# AI Virtual Mouse
<div style="text-align: center;">
    <img src="static/image.png" alt="AI Virtual Mouse" width="500" />
</div>

## Overview
The AI Virtual Mouse project uses a webcam to control the mouse pointer on your computer. By detecting hand gestures, it allows you to move the mouse and perform clicks without touching a mouse.

## Features
- Mouse Movement: Move the cursor using hand gestures.
- Clicking: Perform clicks by pinching your fingers.

## Requirements
Make sure you have the following Python libraries installed:
`opencv-python: For computer vision tasks.`
`numpy: For numerical operations.`
`pyautogui: For controlling the mouse.`
`mediapipe: For hand tracking.`
`Flask: For creating the web interface.`

## Installation
1. Clone the Repository
   
   ```
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Create a Virtual Environment (Optional but recommended)

   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```
3. Install the Requirements

   ```
   pip install -r requirements.txt
   ```

## Running the Project
1. Start the Flask Application

   ```
   python app.py
   ```
   This will start a web server. Open your browser and go to

2. Interact with the Web Interface
On the web page, click the "START" button to begin using the AI Virtual Mouse.
Follow the instructions on the screen to move and click the mouse using hand gestures.

## Troubleshooting
If you encounter issues related to JAX or ml_dtypes, ensure you have the correct versions installed:

Update ml_dtypes
```
pip install --upgrade ml_dtypes
```

Check the Installed Version
```
pip show ml_dtypes
```

## Contributing
Feel free to submit pull requests or open issues if you encounter problems or have suggestions for improvements.
