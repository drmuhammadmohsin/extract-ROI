# Region of Intrest (ROI) Extraction 

# Image Contour Detection and Extraction

This Python script uses OpenCV to detect the largest contour in any image, highlight it, and extract the region of interest (ROI). The script displays and saves the intermediate and final results.

## Features

- **Grayscale Conversion:** Converts the image to grayscale for easier contour detection.
- **Edge Detection:** Uses Canny edge detection to identify edges in the image.
- **Morphological Transformation:** Enhances the detected edges by filling gaps using a closing operation.
- **Contour Detection:** Finds and sorts contours by area, focusing on the largest one.
- **Bounding Box Extraction:** Draws a rectangle around the largest contour and extracts the corresponding ROI.
- **Visualization & Saving:** Displays processed images and saves them as PNG files.

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
## Usage

1. Place your image at the specified path (`specify your image path in local setup`).
2. Run the script.
3. View and save the processed images:
   - `canny.png`: Edge-detected image.
   - `close.png`: Morphologically transformed image.
   - `ROI.png`: Extracted region of interest.
   - `image.png`: Original image with the largest contour highlighted.

