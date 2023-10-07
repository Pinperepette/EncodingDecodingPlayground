#!/usr/bin/env python

import base64

def decode(text):
    decoded_bytes = base64.b32decode(text.encode('utf-8'))
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text
