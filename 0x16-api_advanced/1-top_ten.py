#!/usr/bin/python3
''' Subscribers count'''
import requests


def top_ten(subreddit):

    header = {'User-agent': 'Electronic_Border115'}
    r = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
        headers=header)
    if r.status_code != 200:
        print(None)
        return
    data = r.json()
    a = data.get('data').get('children')
    for i in range(0, 10):
        print(a[i].get('data').get('title'))
