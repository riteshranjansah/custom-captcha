# Custom CAPTCHA

This repository contains a simple Flask-based CAPTCHA application that challenges users to identify the correct rotation of an image. The application generates images with random rotations and asks users to select the correct one based on a reference image.

## Features

- **Dynamic CAPTCHA Generation**: Generates CAPTCHA images with random background colors and characters.
- **User Interaction**: Allows users to navigate through different rotated images to select the correct one.
- **Flask Framework**: Built using Flask, making it easy to run and extend.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Pillow (Python Imaging Library)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/custom-captcha.git
   cd custom-captcha
   ```

2. Install the required packages:
   ```bash
   pip install Flask Pillow
   ```

3. Create a folder named `static` in the root directory, and add a font file named `arial.ttf` to it.

### Running the Application

1. Start the Flask application:
   ```bash
   python custom-captcha/app.py
   ```

2. Open your browser and go to `http://127.0.0.1:5000` to view the CAPTCHA.

## How It Works

1. When the user accesses the main page, a set of images is generated, including a reference image and several rotated images.
2. The user can navigate through the images using the provided buttons.
3. Upon selecting an image and submitting their answer, the application checks if the user's response matches the correct rotation and provides feedback.

## Customization

- You can modify the characters used in the CAPTCHA by changing the `char` variable in the `create_captcha_images` function.
- Adjust the dimensions of the generated images by modifying the `bg_size` parameter in the same function.

## Contributing

If you'd like to contribute to this project, please open an issue or submit a pull request. Contributions are welcome!

## Acknowledgments

- Flask: A lightweight WSGI web application framework.
- Pillow: A powerful image processing library for Python.

## Contact

For any questions or feedback, feel free to reach out via GitHub issues.
