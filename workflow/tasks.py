#!/usr/bin/env python3
import subprocess
import json

try:
    result = subprocess.check_output(
        ["task", "rc.json.array=on", "limit:100", "status:pending", "export"],
        stderr=subprocess.DEVNULL,
        text=True
    )
    tasks = json.loads(result)

    items = [{
        "title": task["description"],
        "subtitle": f'ID: {task.get("id", "—")} | Due: {task.get("due", "N/A")}',
        "arg": str(task["id"])
    } for task in tasks]

except Exception as e:
    items = [{"title": f"🔴 Error: {str(e)}", "valid": False}]

# Добавим переменную для встройки фильтра
print(json.dumps({
    "items": items,
    "variables": {
        "alfredfiltersresults": "true"
    }
}))
