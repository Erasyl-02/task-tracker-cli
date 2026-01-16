from pathlib import Path
import sys
from datetime import datetime
import json
import logic

DB_File = 'database.json'

#command = sys.argv[1]
def main():
    # if len(sys.argv) < 3:
    #     print('type a command')
    #     return
    command = sys.argv[1]
    command2 = sys.argv[2]
    if command == 'add':
        logic.add_task(command2)
    if command == 'list':
        if len(sys.argv) < 3:
            logic.list_task()
        else:
            if command2 == 'done':
                print('this should show done tasks')
            if command2 == 'todo':
                print('this should show task that should be done')
            if command2 == 'in-progress':
                print('these are tasks that are in progress')
    if command == 'delete':
        print('this is delete command')
    if command == 'update':
        print('this is update command')
    if command == 'mark-in-progress':
        print('this is mark-in-progress command')
    if command == 'mark-done':
        print('this is mark-done command')

if __name__ == "__main__":
    main()