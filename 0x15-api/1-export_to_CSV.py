#!/usr/bin/python3
"""Python script to export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    userId = (argv[1])
    respUser = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId))
    respTodos = requests.get(
        "https://jsonplaceholder.typicode.com/todos".format(userId))

    name = respUser.json().get('username')

    with open('{}.csv'.format(userId), 'w', newline='') as csvfile:
        Cwrite = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for item in respTodos.json():
            if item.get('userId') == int(userId):
                Cwrite.writerow(
                    [userId, name, item.get('completed'), item.get('title')])
