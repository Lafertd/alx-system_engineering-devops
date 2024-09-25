#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"
    }
    
    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the subreddit is invalid or inaccessible
        if response.status_code != 200:
            return 0
        
        # Try to parse the JSON response and access the 'data' field
        data = response.json().get("data", {})
        
        # Return the number of subscribers, defaulting to 0 if not found
        return data.get("subscribers", 0)
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors or invalid JSON parsing
        print(f"Error: {e}")
        return 0
