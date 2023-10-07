#!/usr/bin/env python
def encode(text, shift=3):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            encoded_text += shifted_char
        else:
            encoded_text += char
    return encoded_text
