#!/usr/bin/env python

def decode(text, shift=3):
    decoded_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 - shift) % 26 + 97)
            decoded_text += shifted_char
        else:
            decoded_text += char
    return decoded_text