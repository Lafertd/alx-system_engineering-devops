#!/usr/bin/python3
"""1-top_ten.py"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    url =      "https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data").get("children")
    top_10 = "\n".join(post.get("data").get("title") for post in data)
    print(top_10)
