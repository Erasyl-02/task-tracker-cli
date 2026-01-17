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

        if not tasks:
                print("The list is empty")
                return

        for task in tasks:
                id = task['id']
                desc = task['description']
                status = task['status']  
                print(f"[{id}] {desc} — ({status})")

def list_marked(status):
        tasks = storage.load_data()

        if not tasks:
                print("The list is empty")
                return
        
        for task in tasks:
                if task['status'] == status:
                        print(f"[{task['id']}] {task['description']} — ({status})")

def update_task(task_id, changes):
        if not changes:
                print('Type updates')
                return
        
        tasks = storage.load_data()

        for task in tasks:
                if task['id'] == int(task_id):
                        task['description'] = changes
                        storage.save_data(tasks)
                        print(f'Task with ID:{task_id} has been updated')
                        return

        print(f'Task with ID:{task_id} doesnt exist')

def mark_task(task_id, change):
        tasks = storage.load_data()

        for task in tasks:
                if task['id'] == int(task_id):
                        task['status'] = change
                        task['updatedAt'] = datetime.now().isoformat()
                        storage.save_data(tasks)
                        print(f'Task with ID:{task_id} marked as {change}')
                        return
        
        print(f'Task with ID:{task_id} doesnt exist')