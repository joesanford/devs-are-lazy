import time
import os

import requests
from requests.auth import HTTPBasicAuth

base_url = 'https://api.github.com/search/issues?q=+language:{language}+state:{state}+type:{type}+archived:false'
languages = ['python', 'javascript', 'css', 'ruby', 'java', 'go', 'php', 'c', 'c++', 'swift', 'shell', 'objective-c']
states = ['open', 'closed']
types = ['pr', 'issue']
github_token = os.environ.get('GITHUB_TOKEN')
github_username = os.environ.get('GITHUB_USERNAME')

data = {}


def get_data():
    for language in languages:
        data[language] = {}
        for type in types:
            data[language][type] = {}
            for state in states:
                time.sleep(2) # to avoid GitHub Search API Rate Limits: https://developer.github.com/v3/search/#rate-limit
                r = requests.get(base_url.format(language=language, type=type, state=state),
                                 auth=HTTPBasicAuth(github_username, github_token))
                data[language][type][state] = r.json().get('total_count', r.text)

    return data


def get_mocked_data():
    return {'python': {'pr': {'open': 159723, 'closed': 3079050}, 'issue': {'open': 1528487, 'closed': 2919859}}, 'javascript': {'pr': {'open': 539227, 'closed': 5790580}, 'issue': {'open': 2361186, 'closed': 3950643}}, 'css': {'pr': {'open': 57471, 'closed': 872585}, 'issue': {'open': 248292, 'closed': 460819}}, 'ruby': {'pr': {'open': 521155, 'closed': 2280152}, 'issue': {'open': 369578, 'closed': 977661}}, 'java': {'pr': {'open': 139682, 'closed': 2916285}, 'issue': {'open': 2185928, 'closed': 4174197}}, 'go': {'pr': {'open': 26750, 'closed': 762512}, 'issue': {'open': 193987, 'closed': 476020}}, 'php': {'pr': {'open': 90126, 'closed': 1707521}, 'issue': {'open': 756084, 'closed': 2101087}}, 'c': {'pr': {'open': 47574, 'closed': 725236}, 'issue': {'open': 1133153, 'closed': 1613625}}, 'c++': {'pr': {'open': 47574, 'closed': 725236}, 'issue': {'open': 1133153, 'closed': 1613625}}, 'swift': {'pr': {'open': 25325, 'closed': 216524}, 'issue': {'open': 66887, 'closed': 137565}}, 'shell': {'pr': {'open': 34215, 'closed': 552111}, 'issue': {'open': 178617, 'closed': 393265}}, 'objective-c': {'pr': {'open': 23845, 'closed': 253407}, 'issue': {'open': 288751, 'closed': 501042}}}