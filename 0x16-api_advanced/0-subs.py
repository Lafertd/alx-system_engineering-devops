#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers or 0 if the subreddit is invalid.
    """
    # Define the URL for the subreddit's about information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set the headers with a custom User-Agent
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyRedditBot/1.0)'}

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data.get('data', {}).get('subscribers', 0)
    except Exception:
        # In case of any error, return 0
        pass
    
    # If not a valid subreddit, return 0
    return 0
