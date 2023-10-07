#!/usr/bin/env python

import base64

def decode(encoded_text):
    decoded_text = base64.b64decode(encoded_text.encode()).decode()
    return decoded_text
