#!/usr/bin/python3
"""
Export data to JSON format
"""

import json
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

    dictionary = {employee_id: []}
    for task in todo:
        dictionary[employee_id].append({
                                        "task": task.get('title'),
                                        "completed": task.get('completed'),
                                        "username": username
                                        })
    with open('{}.json'.format(employee_id), 'w') as json_file:
        json.dump(dictionary, json_file)
