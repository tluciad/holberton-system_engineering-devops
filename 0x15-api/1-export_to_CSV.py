#!/usr/bin/python3
"""Python script to export data in the CSV format"""
import requests
from sys import argv
import csv

if __name__ == "__main__":

    userId = (argv[1])
    response_user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId)).json()
    response_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos".format(userId)).json()

    USERNAME = response_user['name']

    with open('USER_ID.csv', 'w', newline='') as csvfile:
        for items in response_todos:
            Uid = items['userId']
            if (Uid == int(userId)):
                TASK_COMPLETED_STATUS = items['completed']
                TASK_TITLE = items['title']
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|',
                                        quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(
                    [f'"{userId}"', f'"{USERNAME}"',
                        f'"{TASK_COMPLETED_STATUS}"', f'"{TASK_TITLE}"'])
