#!/usr/bin/python3
''' Subscribers count'''
import requests


def number_of_subscribers(subreddit):

    header = {'User-agent': 'Electronic_Border115'}
    r = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers=header)
    if r.status_code != 200:
        return 0
    data = r.json()
    return(data.get('data').get('subscribers'))
