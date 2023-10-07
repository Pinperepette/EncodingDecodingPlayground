#!/usr/bin/env python

def encode(text):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    return binary_text
