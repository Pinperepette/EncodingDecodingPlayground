#!/usr/bin/env python

def decode(encoded_text):
    decoded_text = ""
    for char in encoded_text:
        if char.isalpha():
            shifted = ord(char) - 13
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            else:
                if shifted < ord('A'):
                    shifted += 26
            decoded_text += chr(shifted)
        else:
            decoded_text += char
    return decoded_text