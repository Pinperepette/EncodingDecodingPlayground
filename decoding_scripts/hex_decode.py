#!/usr/bin/env python

def decode(encoded_text):
    try:
        decoded_text = bytes.fromhex(encoded_text).decode('utf-8')
        return decoded_text
    except ValueError:
        return "Invalid Hexadecimal String"
