#!/usr/bin/python3
""" Module that queries the Reddit API and returns the number of subscribers """
import requests
import sys
def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    x = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    if x.status_code == 200:
        print(x.json()['data']['subscribers'])
    else:
        print(0)
