#!/usr/bin/env python

from flask import Flask, render_template, request
import os
import importlib.util
import base64

app = Flask(__name__)

def load_encoding_scripts_from_folder(folder_path):
    scripts = {}
    for script_file in os.listdir(folder_path):
        if script_file.endswith("_encode.py"):
            script_name = os.path.splitext(script_file)[0]
            spec = importlib.util.spec_from_file_location(script_name, os.path.join(folder_path, script_file))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "encode"):
                scripts[script_name] = module.encode
    return scripts

def load_decoding_scripts_from_folder(folder_path):
    scripts = {}
    for script_file in os.listdir(folder_path):
        if script_file.endswith("_decode.py"):
            script_name = os.path.splitext(script_file)[0]
            spec = importlib.util.spec_from_file_location(script_name, os.path.join(folder_path, script_file))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "decode"):
                scripts[script_name] = module.decode
    return scripts

def base64_encode_text(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text

def base64_decode_text(text):
    decoded_bytes = base64.b64decode(text.encode('utf-8'))
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text

def decode_text_with_script(script_name, encoded_text):
    if script_name == 'base64_decode':
        return base64_decode_text(encoded_text)
    elif script_name in decoding_scripts:
        decoding_function = decoding_scripts[script_name]
        return decoding_function(encoded_text)
    else:
        return "Decoding script not found."

encoding_scripts = load_encoding_scripts_from_folder("encoding_scripts")
decoding_scripts = load_decoding_scripts_from_folder("decoding_scripts")

@app.route('/')
def index():
    return render_template('index.html', encoding_scripts=encoding_scripts, decoding_scripts=decoding_scripts)

@app.route('/encode', methods=['POST'])
def encode():
    script_name = request.form['script']
    text = request.form['text']
    if script_name == 'base64_encode':
        encoded_text = base64_encode_text(text)
    elif script_name in encoding_scripts:
        encoding_function = encoding_scripts[script_name]
        encoded_text = encoding_function(text)
    else:
        return "Encoding script not found."
    return encoded_text

@app.route('/decode', methods=['POST'])
def decode():
    script_name = request.form['script']
    encoded_text = request.form['text']
    decoded_text = decode_text_with_script(script_name, encoded_text)
    return decoded_text

if __name__ == '__main__':
    app.run(debug=True)
