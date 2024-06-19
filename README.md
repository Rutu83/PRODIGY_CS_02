# Image Encryptor/Decryptor

This project is a graphical user interface (GUI) application for encrypting and decrypting images using a pseudo-random number generator (PRNG). The application is built using Python and the Tkinter library.

## Features

- **Image Loading**: Load images in JPEG, JPG, and PNG formats.
- **Encryption**: Encrypt images using a secure method based on a numeric key.
- **Decryption**: Decrypt previously encrypted images using the correct numeric key.
- **Error Handling**: Proper error messages for incorrect decryption keys and invalid inputs.

## Installation

### Prerequisites

- Python 3.x
- Required Python packages:
  - numpy
  - Pillow
  - tkinter (usually included with Python)

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/image-encryptor-decryptor.git
    cd image-encryptor-decryptor
    ```

2. **Install the required packages**:
    ```bash
    pip install numpy pillow
    ```

## Usage

1. **Run the application**:
    ```bash
    python Image_Encription.py
    ```

2. **Load an Image**:
    - Click on the "Respective(encript/decript)" button to select an image file.

3. **Encrypt an Image**:
    - Enter a numeric key in the "Enter Key" field under the "Encryption" section.
    - Click on the "Encrypt" button.
    - Choose a location to save the encrypted image.

4. **Decrypt an Image**:
    - Enter the same numeric key used for encryption in the "Enter Key" field under the "Decryption" section.
    - Click on the "Decrypt" button.
    - Choose a location to save the decrypted image.
    - If the key is incorrect, an error message will be displayed.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The application uses the Tkinter library for the GUI.
- Image processing is done using the Pillow and numpy libraries.



