import sys
import json
import pathlib
from datetime import datetime

import storage


def add_task(desc):
        tasks = storage.load_data()
        new_task = {
        "id": len(tasks) + 1,
        "description": desc,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
        }
        
        tasks.append(new_task)
        storage.save_data(tasks)
        print(f'your task has been added')

def list_task():
        tasks = storage.load_data()
        count = 0
        for i in tasks:
                print(i[count])
                count += 1

