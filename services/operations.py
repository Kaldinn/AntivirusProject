from flask import jsonify
import os
import hashlib
import pyclamd


#NotUsedYet
def scan_file_clamav(file_path):
    cd = pyclamd.ClamdAgnostic()
    scan_result = cd.scan_file(file_path)
    return scan_result

def calculate_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def scan_file_content(content):
    keywords = ['malware', 'virus', 'threat', 'dangerous']
    for keyword in keywords:
        if keyword in content:
            return f"Potencjalnie zagrożony plik! Znaleziono słowo kluczowe: {keyword}"
    return "Plik bezpieczny"

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()