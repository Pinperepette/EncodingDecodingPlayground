#!/usr/bin/env python
def encode(text):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + 13
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            else:
                if shifted > ord('Z'):
                    shifted -= 26
            encoded_text += chr(shifted)
        else:
            encoded_text += char
    return encoded_text