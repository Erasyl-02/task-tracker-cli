import json
import pathlib

DB_File = 'data.json'

def load_data():
    try:
        with open(DB_File, 'r', encoding = 'utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_data(tasks):
    with open(DB_File, 'w', encoding = 'utf-8') as f:
        json.dump(tasks, f, indent = 4)
