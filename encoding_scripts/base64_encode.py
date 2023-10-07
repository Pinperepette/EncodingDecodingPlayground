#!/usr/bin/env python

import base64

def encode(text):
    encoded_text = base64.b64encode(text.encode()).decode()
    return encoded_text
