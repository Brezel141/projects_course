# QR Code Generator

This Python script generates QR codes. The user can specify the text to be encoded in the QR code, and the script will generate a QR code image file.

## How It Works

The script uses the `qrcode` module to generate QR codes. The user is prompted to enter the text they want to encode in the QR code.

The script then generates a QR code that encodes the user's text. The QR code is saved as an image file with a specified filename, foreground color, and background color.

## Usage

Simply run the script, and enter the text you want to encode in the QR code when prompted. The script will generate a QR code and save it as 'sample.png' with a black foreground and white background.

## Example

```bash
Enter text: Hello, world!
Successfully created! (sample.png)