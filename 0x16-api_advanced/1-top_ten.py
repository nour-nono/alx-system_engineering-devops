#!/usr/bin/python3
""" Module that queries the Reddit API and prints the titles 
of the first 10 hot posts listed for a given subreddit. """
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    x = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    if x.status_code == 200:
        try:
            for i in range(10):
                print(x.json()['data']['children'][i]['data']['title'])
        except KeyError:
            print(None)
    else:
        print(None)
