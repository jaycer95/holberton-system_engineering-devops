#!/usr/bin/python3
"""Python script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress """
import json
import requests
from sys import argv


if __name__ == "__main__":
    TUID = {'userId': argv[1]}
    TID = {'id': argv[1]}
    r1 = requests.get(
        url="https://jsonplaceholder.typicode.com/todos",
        params=TUID)
    r2 = requests.get(
        url="https://jsonplaceholder.typicode.com/users",
        params=TID)
    todo = r1.json()
    user = r2.json()

    for usr in user:
        USERNAME = usr.get('username')
        USER_ID = usr.get('id')
    FILE = str(USER_ID) + '.json'
    data = {USER_ID: []}
    with open(FILE, mode='w') as f:
        for tasks in todo:
            dic = {}
            dic["task"] = tasks.get('title')
            dic["completed"] = tasks.get('completed')
            dic["username"] = USERNAME
            data[USER_ID].append(dic)
        json.dump(data, f)
