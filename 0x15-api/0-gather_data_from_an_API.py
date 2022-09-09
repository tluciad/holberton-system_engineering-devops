#!/usr/bin/python3
""" Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    """module to returns information about his/her TODO list"""

    employee = (sys.argv[1])
    users_url = f"https://jsonplaceholder.typicode.com/users/{employee}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos"

    response_user = requests.get(users_url).json()
    response_todos = requests.get(todos_url).json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    Title = []
    EMPLOYEE_NAME = response_user['name']

    for items in response_todos:
        U_id = items['userId']
        if (U_id == int(employee)):
            TOTAL_NUMBER_OF_TASKS += 1
            if (items['completed'] is True):
                Title.append(items['title'])
                NUMBER_OF_DONE_TASKS += 1

    print(
        f"Employee {EMPLOYEE_NAME} is done with tasks\
            ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for title in Title:
        print(f"\t{title}")
