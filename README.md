# EncodingDecodingPlayground
Text Encoding/Decoding Web App

## Text Encoding/Decoding Web App

This is a simple web application built with Flask that allows users to perform text encoding and decoding. What sets this app apart is its ability to automatically recognize and utilize scripts placed in designated folders, providing a seamless experience for adding new encoding and decoding methods.

## Adding New Scripts

To add new encoding or decoding scripts, refer to the structure of the existing scripts in the `decoding_scripts` and `encoding_scripts` folders. Simply create new Python files with your encoding and decoding functions inside these folders. The web application will automatically detect and include them in the dropdown menus for users to choose from.

## Rules for Adding Custom Scripts

To add new encoding or decoding methods, follow these rules:

1. **File Naming:** Name your Python script ending with `_encode.py` for encoding or `_decode.py` for decoding. For example: `my_script_encode.py`, `custom_decode.py`.

2. **Script Functions:** Ensure your Python script contains a function named `encode(text)` for encoding or `decode(text)` for decoding. These functions should accept a string input (`text`) and return the encoded or decoded string.

3. **Folder Placement:** Place your encoding scripts in the `encoding_scripts` directory and decoding scripts in the `decoding_scripts` directory.


![Alt Text](https://github.com/Pinperepette/EncodingDecodingPlayground/blob/main/imm.png)
