#!/usr/bin/env python

import base64

def encode(text):
    encoded_bytes = base64.b32encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text