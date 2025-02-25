# Batch-Bg-remover

Description:
This Python tool allows you to remove the background from images using the Remove.bg API. It supports both single-image and batch processing with the ability to enhance the images before processing. The tool uses the tkinter library for a graphical user interface (GUI) that makes it easy to select input images, specify output locations, and perform background removal.

Requirements:
1. Python 3.x
2. PIL (Pillow) - Python Imaging Library
3. requests - HTTP library for making requests to the Remove.bg API
4. tkinter - Standard GUI library in Python (may need to be installed separately depending on the environment)

Installation:
1. Install Python (if not already installed).
2. Install the required libraries using pip:
   pip install Pillow requests

Usage:
1. Run the script to launch the GUI.
2. The main window will display two buttons:
   - "Remove Background (Single)": Process a single image.
   - "Remove Background (Batch)": Process multiple images at once.
3. After selecting images:
   - For Single Image: Choose an image file, then select where to save the processed image with the background removed.
   - For Batch Processing: Select multiple images, and specify a folder where all processed images will be saved.
4. The tool will enhance the image by adjusting contrast, sharpening it, and resizing if necessary before removing the background using the Remove.bg API.

Configuration:
- You need an API key from Remove.bg for background removal. Replace the value of REMOVE_BG_API_KEY with your personal API key:
   REMOVE_BG_API_KEY = 'YOUR_API_KEY_HERE'

Troubleshooting:
- If an image is too small, the program will automatically resize it for better processing.
- If you encounter any errors, a message box will appear with the error details.

Contact:
For any issues, please contact me or refer to the official documentation for the Remove.bg API.

