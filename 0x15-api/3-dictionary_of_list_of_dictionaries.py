#!/usr/bin/python3
"""extend your Python script to export data in the JSON format."""
import json
import requests


if __name__ == "__main__":

    respUser = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    respTodos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    NewDictionary = {}
    for user in respUser:
        tasks = []
        for item in respTodos:
            if user.get('id') == item.get('userId'):
                tskDictionary = {"username": user.get('username'),
                                 "task": item.get('title'),
                                 "completed": item.get('completed')}
                tasks.append(tskDictionary)
        NewDictionary[user.get('id')] = tasks
        with open("todo_all_employees.json", 'w') as Jfile:
            json.dump(NewDictionary, Jfile)
