#!/usr/bin/python3
"""Python script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress """
import csv
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
        USER_ID = usr.get("id")
        USERNAME = usr.get("username")
    file = str(USER_ID) + ".csv"
    with open(file, mode='w') as f:
        d = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for tasks in todo:
            TASK_STATUS = tasks.get("completed")
            TASK_TITLE = tasks.get("title")
            d.writerow([USER_ID, USERNAME, TASK_STATUS, TASK_TITLE])
