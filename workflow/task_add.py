#!/usr/bin/env python3
import sys
import subprocess
import json

task_desc = sys.argv[1]
subprocess.run(["task", "add", task_desc])

print(json.dumps({
    "items": [{
        "title": f"✅ Добавлена задача: {task_desc}",
        "valid": False
    }]
}))
