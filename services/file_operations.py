import subprocess
import os

def display_files(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)
    return result.stdout

def display_current_path():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return current_dir