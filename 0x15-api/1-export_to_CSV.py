#!/usr/bin/python3
"""
Exports to CSV
"""

import csv
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = (
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
            )

    response = requests.get(user_url)
    username = response.json().get('username')

    response = requests.get(todo_url)
    todo = response.json()
    with open(f"{employee_id}.csv", 'w') as csvfile:
        for task in todo:
            completed = task.get('completed')
            title = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'
                          .format(employee_id, username, completed, title))
