#!/usr/bin/python3
""" Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress."""
import requests
from sys import argv
if __name__ == "__main__":
    """module to returns information about his/her TODO list"""
    userId = (argv[1])

    response_user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId)).json()
    response_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos".format(userId)).json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    Title = []
    EMPLOYEE_NAME = response_user['name']

    for items in response_todos:
        U_id = items['userId']
        if (U_id == int(userId)):
            TOTAL_NUMBER_OF_TASKS += 1
            if (items['completed'] is True):
                Title.append(items['title'])
                NUMBER_OF_DONE_TASKS += 1

    print(f"Employee {EMPLOYEE_NAME} is done with tasks\
            ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for title in Title:
        print(f"\t{title}")
