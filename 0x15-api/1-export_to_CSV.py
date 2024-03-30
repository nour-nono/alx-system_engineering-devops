#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
and saves it to a CSV file."""
import requests
import sys
import csv

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
    with open(f"{sys.argv[1]}.csv", "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([sys.argv[1], data.get("username"),
                             todo.get("completed"), todo.get("title")])
