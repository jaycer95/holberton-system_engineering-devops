#!/usr/bin/python3
''' Subscribers count'''
import requests


def recurse(subreddit, hot_list=[], after=''):

    header = {'User-agent': 'Electronic_Border115'}
    r = requests.get(
        'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after),
        headers=header)
    if r.status_code != 200:
        print(None)
        return
    data = r.json()
    d = data.get('data')
    c = d.get('children')
    for i in c:
        hot_list.append(i.get('data').get('title'))
    after = d.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
