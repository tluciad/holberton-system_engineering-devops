#!/usr/bin/python3
"""extend your Python script to export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    respUser = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId))
    respTodos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    name = respUser.json().get('username')
    Newdict = {}
    List = []

    for item in respTodos:
        if item.get('userId') == int(userId):
            tk_dict = {"task": item.get('title'),
                       "completed": item.get('completed'), "username": name}
            List.append(tk_dict)
    Newdict[userId] = List
    with open("{}.json".format(userId), 'w') as Jfile:
        json.dump(Newdict, Jfile)
