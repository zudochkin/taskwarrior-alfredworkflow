#!/usr/bin/env python3
import sys
import subprocess
import json

task_id = sys.argv[1]
subprocess.run(["task", task_id, "done"])

print(json.dumps({
    "items": [{
        "title": f"✅ Задача {task_id} завершена",
        "valid": False
    }]
}))
