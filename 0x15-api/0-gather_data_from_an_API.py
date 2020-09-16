#!/usr/bin/python3
"""Python script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress """
import requests
from sys import argv

if __name__ == "__main__":
    TUID = {'userId': argv[1]}
    TID = {'id': argv[1]}
    r1 = requests.get(
        url="https://jsonplaceholder.typicode.com/todos",
        params=TUID)
    r2 = requests.get(url="https://jsonplaceholder.typicode.com/users", params=TID)
    todo = r1.json()
    user = r2.json()

    done = 0
    for task in todo:
        if task.get("completed"):
            done += 1
    for info in user:
        name = info.get("name")
    print("Employee {} is done with tasks({}/{}):".format(
        name, done, len(todo)))
    for task in todo:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
