#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit. If an
invalid subreddit is given, the function should return 0.
"""


def top_ten(subreddit):
    """ does what is stated above """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json?limit=9'.format(subreddit)
    request = requests.get(url,
                           headers={'User-Agent': 'Mike'},
                           allow_redirects=False)
    if request.status_code != 200:
        print (None)
        return None
    request = request.json()
    if 'data' in request:
        for post in request.get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
        return None
