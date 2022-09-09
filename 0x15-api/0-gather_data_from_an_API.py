#!/usr/bin/python3
""" Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress."""
import requests
from sys import argv


if __name__ == "__main__":

    userId = (argv[1])
    respUser = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId))
    respTodos = requests.get(
        "https://jsonplaceholder.typicode.com/todos".format(userId))

    taskcompleted = 0
    totalnumtask = 0
    name = respUser.json().get('name')
    Title = []

    for item in respTodos.json():
        if item.get('userId') == int(userId):
            totalnumtask += 1
            if item.get('completed'):
                taskcompleted += 1

    print("Employee {} is done with tasks({}/{}):".format(name,
          taskcompleted, totalnumtask))

    print('\n'.join(["\t " + item.get('title') for item in respTodos.json()
          if item.get('userId') == int(userId) and item.get('completed')]))
