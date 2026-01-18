from pathlib import Path
import sys
from datetime import datetime

import logic


def main():
    if len(sys.argv) < 3 and sys.argv[1] != 'list':
         print('type a command')
         return
    command = sys.argv[1]
    if command == 'add':
        command2 = sys.argv[2]
        logic.add_task(command2)
    if command == 'list':
        if len(sys.argv) < 3:
            logic.list_task()
            return
        else:
            command2 = sys.argv[2]
            if command2 in ['done', 'todo', 'in-progress']:
                logic.list_marked(command2)
    command2 = sys.argv[2]
    if command == 'delete':
        logic.delete_task(command2)
    if command == 'update':
        if len(sys.argv) < 4:
            print('You should type changes')
            return
        logic.update_task(command2, sys.argv[3])
    if command == 'mark-in-progress':
        logic.mark_task(command2, 'in-progress')
    if command == 'mark-done':
        logic.mark_task(command2, 'done')

if __name__ == "__main__":
    main()