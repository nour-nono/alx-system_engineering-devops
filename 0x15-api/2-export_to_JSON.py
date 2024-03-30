#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
and saves it to a json file."""
import json
import requests
import sys

if __name__ == "__main__":
    u = f"https://jsonplaceholder.typicode.com/"
    response = requests.get(u+f"users/{sys.argv[1]}")
    data = response.json()
    p = {"userId": sys.argv[1], "completed": "true"}
    pp = {"userId": sys.argv[1]}
    todos = requests.get(url=u+"todos", params=pp).json()
    with open(f"{sys.argv[1]}.json", "w") as f:
        json.dump({sys.argv[1]: [{"task": todo.get("title"),
                                  "completed": todo.get("completed"),
                                  "username": data.get("username")}
                                 for todo in todos]}, f)
