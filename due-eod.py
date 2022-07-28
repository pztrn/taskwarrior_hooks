#!/usr/bin/env python3

# TaskWarrior's hook that sets due date to the end of date.
# By default TaskWarrior sets it to 00:00:00.

import datetime
import json
import sys


def get_task_data() -> str:
    """
    Gets task data from stdin.

    It might be first line on task addition and second line on task modification.

    :return: str
    """
    input_data = sys.stdin.readlines()

    with open("/Users/pztrn/TEMP/abracadabra", "w") as f:
        f.write(input_data[-1])

    return input_data[-1]


task_data_raw = get_task_data()

task_data = json.loads(task_data_raw)

if "due" in task_data:
    new_due_ts = datetime.datetime.strptime(task_data["due"], "%Y%m%dT%H%M%S%z").astimezone()
    if new_due_ts.hour == 00 and new_due_ts.minute == 00 and new_due_ts.second == 00:
        new_due_ts = new_due_ts.replace(hour = 23, minute = 59, second = 59)

    task_data["due"] = new_due_ts.astimezone(tz = datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

print(json.dumps(task_data, ensure_ascii = False))
sys.exit(0)
