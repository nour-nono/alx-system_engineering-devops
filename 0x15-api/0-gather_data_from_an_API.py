#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID"""
import requests
import sys

x = sys.argv[1]

if __name__ == "__main__":
    u = f"https://jsonplaceholder.typicode.com/"
    response = requests.get(u+f"users/{x}")
    data = response.json()
    p = {"userId": x, "completed": "true"}
    pp = {"userId": x}
    todos = requests.get(url=u+"todos", params=p).json()
    print(f"Employee {data.get('name')} is done with"
          f" tasks({len(todos)}/"
          f"{len(requests.get(url=u+"todos", params=pp).json())}):")
    for todo in todos:
        print("\t " + todo.get("title"))
