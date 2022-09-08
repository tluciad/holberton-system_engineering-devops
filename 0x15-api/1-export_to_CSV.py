#!/usr/bin/python3
import requests
import sys
import csv

if __name__ == "__main__":

    USER_ID = (sys.argv[1])
    users_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos"

    response_user = requests.get(users_url).json()
    response_todos = requests.get(todos_url).json()

    USERNAME = response_user['name']

    with open('USER_ID.csv', 'w', newline='') as csvfile:
        for items in response_todos:
            Uid = items['userId']
            if (Uid == int(USER_ID)):
                TASK_COMPLETED_STATUS = items['completed']
                TASK_TITLE = items['title']
                spamwriter = csv.writer(
                    csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(
                    [f'"{USER_ID}"', f'"{USERNAME}"', f'"{TASK_COMPLETED_STATUS}"', f'"{TASK_TITLE}"'])
