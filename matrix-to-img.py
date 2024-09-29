"""
This Streamlit app displays live video from the default camera, converting each
frame to grayscale and displaying it in a table format.
The app also continuously updates the video stream, allowing for real-time
viewing.
"""

# -- Standard Imports

# -- Third-Party Imports

# -- Local Imports

import cv2  # OpenCV library for image processing
import streamlit as st


__author__ = "Mike Salem"
__email__ = "mike.f.salem@gmail.com"


def mat(cap: cv2.VideoCapture) -> None:
    """
    Display a single frame from the video stream as a dataframe image.

    Parameters:
        cap (cv2.VideoCapture): Video capture object

    Returns:
        None
    """

    # Read a frame from the video stream
    ret, frame = cap.read()

    if ret:  # If frame is read successfully
        # Convert the frame from BGR to RGB
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the in table format
        with placeholder.container():
            st.dataframe(gray_img)


def t(cap: cv2.VideoCapture) -> None:
    """
    Continuously display frames from the video stream as grayscale images.

    Parameters:
        cap (cv2.VideoCapture): Video capture object

    Returns:
        None
    """

    # Read a frame from the video stream
    ret, frame = cap.read()

    if ret:  # If frame is read successfully
        # Convert the frame from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the grayscale image in a placeholder widget
        with video_placeholder.container():
            video_placeholder.image(
                rgb_frame, channels="GRAY", use_column_width=True)


def main() -> None:
    """
    Main function that initializes and runs the video streaming.

    Returns:
        None
    """

    # Create a video capture object to access the default camera (index 0)
    cap = cv2.VideoCapture(0)

    while True:  # Continuously update the video stream
        mat(cap)  # Display a single frame as a dataframe
        t(cap)  # Continuously display frames as grayscale images

    # Release the video capture object to free up resources
    cap.release()

    # Return from main function


if __name__ == "__main__":
    st.title("What does a computer 'see'?")

    # Create tabs for "Computer" and "Human"
    computer, human = st.tabs(["Computer", "Human"])

    # Initialize an empty widget for the grayscale image
    with computer:
        placeholder = st.empty()

    # Initialize an empty widget for the video stream
    with human:
        video_placeholder = st.empty()

    main()
