#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for successful request
        if response.status_code != 200:
            print("None")
            return

        # Parse the JSON response
        data = response.json().get("data", {}).get("children", [])

        # Check if the posts exist
        if not data:
            print("None")
            return

        # Print the titles of the first 10 posts
        for post in data:
            print(post.get("data", {}).get("title"))

    except Exception as e:
        print("None")


# Example usage
if __name__ == "__main__":
    top_ten("learnpython")
