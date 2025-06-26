#!/usr/bin/env python3
import sys
import subprocess
import json
import shlex

task_input = sys.argv[1]
# Split the input to allow taskwarrior to parse attributes like project:work
cmd = ["task", "add"] + shlex.split(task_input)
subprocess.run(cmd)

print(json.dumps({
    "items": [{
        "title": f"✅ Task added: {task_input}",
        "valid": False
    }]
}))
