#!/usr/bin/python3
"""Python script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress """
import json
import requests
from sys import argv

if __name__ == "__main__":
    r1 = requests.get('https://jsonplaceholder.typicode.com/todos/')
    r2 = requests.get('https://jsonplaceholder.typicode.com/users')
    todo = r1.json()
    user = r2.json()
    dic = {}
    with open('todo_all_employees' + '.json', mode='w') as f:
        for users in user:
            USERNAME = users.get("username")
            Id = users.get("id")
            dic[Id] = []
            for tasks in todo:
                if Id == tasks["userId"]:
                    inside = {}
                    inside = {"username": USERNAME, "task": tasks.get("title"),
                              "completed": tasks.get("completed")}
                    dic[Id].append(inside)
        json.dump(dic, f)
