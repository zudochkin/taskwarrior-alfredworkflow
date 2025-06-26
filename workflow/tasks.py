#!/usr/bin/env python3
import subprocess
import json
from datetime import datetime

def format_due_date(due_str):
    if not due_str or due_str == "N/A":
        return "N/A"
    try:
        # Parse taskwarrior ISO format: 20250626T205959Z
        dt = datetime.strptime(due_str, "%Y%m%dT%H%M%SZ")
        return dt.strftime("%Y-%m-%d %H:%M")
    except:
        return due_str

try:
    result = subprocess.check_output(
        ["task", "rc.json.array=on", "limit:100", "status:pending", "export"],
        stderr=subprocess.DEVNULL,
        text=True
    )
    tasks = json.loads(result)

    items = []
    for task in tasks:
        project = task.get("project", "")
        due_formatted = format_due_date(task.get("due"))
        
        subtitle_parts = [f'ID: {task.get("id", "—")}']
        if project:
            subtitle_parts.append(f'Project: {project}')
        subtitle_parts.append(f'Due: {due_formatted}')
        
        items.append({
            "title": task["description"],
            "subtitle": " | ".join(subtitle_parts),
            "arg": str(task.get("id", ""))
        })

except Exception as e:
    items = [{"title": f"🔴 Error: {str(e)}", "valid": False}]

# Добавим переменную для встройки фильтра
print(json.dumps({
    "items": items,
    "variables": {
        "alfredfiltersresults": "true"
    }
}))
