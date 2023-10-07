#!/usr/bin/env python

def decode(text):
    binary_values = text.split()
    decoded_text = ''.join(chr(int(bv, 2)) for bv in binary_values)
    return decoded_text
