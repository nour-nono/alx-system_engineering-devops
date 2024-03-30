#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    u = f"https://jsonplaceholder.typicode.com/"
    response = requests.get(u+f"users/{sys.argv[1]}")
    data = response.json()
    p = {"userId": sys.argv[1], "completed": "true"}
    pp = {"userId": sys.argv[1]}
    todos = requests.get(url=u+"todos", params=p).json()
    print(f"Employee {data.get('name')} is done with"
          + " tasks({len(todos)}/"
          + f"{len(requests.get(url=u+"todos", params=pp).json())}):")
    for todo in todos:
        print("\t " + todo.get("title"))
