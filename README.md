**Streaming Camera Matrix and Grayscale Streamlit App**
==========================

A simple Streamlit app that displays live video from the default camera, converting each frame to grayscale and displaying it in a table format.

**Features**

* Real-time video streaming
* Live video feed from default camera
* Grayscale conversion of each frame for easy viewing
* Continuously updated video stream
* Option to display single frame as dataframe image

**Usage**
-------

1. Clone this repository using `git clone https://github.com/your-username/matrix-to-img.git`
2. Run the app using `streamlit run grayscale_video_streamlit_app.py` (assuming you've installed Streamlit)
3. Open a web browser and navigate to `http://localhost:8501` to view the live video feed

**Code Structure**
-----------------

The code is organized into three functions:

* **mat**: Displays a single frame from the video stream as a dataframe image.
* **t**: Continuously displays frames from the video stream as grayscale images.
* **main**: Main function that initializes and runs the video streaming.

**Authors**
----------

This app was created by Mike Salem (`mike.f.salem@gmail.com`). Contributions and feedback welcome!

**Notes**

* The app uses OpenCV for image processing and Streamlit for the front-end interface.
* The `mat` function displays a single frame as a dataframe image, while the `t` function continuously updates the video stream with grayscale images.
* The main function initializes and runs the video streaming loop.

You can run this code by cloning the repository and running the `streamlit run` command. Open a web browser to view the live video feed.
