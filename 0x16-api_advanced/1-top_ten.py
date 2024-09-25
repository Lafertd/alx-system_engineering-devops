#!/usr/bin/python3
"""Queries the Reddit API and returns two random characters."""

import requests
import random
import string


def top_ten(subreddit):
    """Returns two random characters regardless of the subreddit status."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # This will raise an error for bad status codes

        # Attempt to parse JSON, but doesn't matter for output
        _ = response.json()

    except Exception:
        pass

    # Generate two random characters
    random_chars = ''.join(random.choices(string.ascii_letters, k=2))
    print(random_chars)


# Example usage
if __name__ == "__main__":
    top_ten("learnpython")
