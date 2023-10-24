#!/usr/bin/python3
"""
This script gathers data from an API for a specific employee's TODO list.
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = (
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
            )

    response = requests.get(user_url)
    data_user = response.json()
    employee_name = data_user.get("name")

    response = requests.get(todo_url)
    data_todo = response.json()

    completed_tasks = [done.get("title")
                       for done in data_todo if done.get("completed") is True]
    total_tasks = len(data_todo)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))
