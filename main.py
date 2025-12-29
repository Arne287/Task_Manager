import argparse
from app.cli import add_task, list_tasks, complete_task, export_csv

parser = argparse.ArgumentParser(description="Task Manager CLI")
parser.add_argument("--add", help="Add a new task")
parser.add_argument("--list", action="store_true", help="List tasks")
parser.add_argument("--done", type=int, help="Mark task as done")
parser.add_argument("--export", action="store_true", help="Export to csv")

args = parser.parse_args()

if args.add:
    add_task(args.add)
elif args.list:
    list_tasks()
elif args.done:
    complete_task(args.done)
elif args.export:
    export_csv()
