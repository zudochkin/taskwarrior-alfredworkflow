#!/usr/bin/env python3
import sys
import subprocess
import json

task_desc = sys.argv[1]
print(task_desc)
subprocess.run(["task", "add", task_desc])
cmd = ["task", "add", task_desc]
print(cmd)
subprocess.run(cmd)

print(json.dumps({
    "items": [{
        "title": f"✅ Task added: {task_desc}",
        "valid": False
    }]
}))
