#!/usr/bin/python3
"""
listing 10 commits of the repository and user
sent in as arguments
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commited in commits[:10]:
        print(commited.get('sha'), end=': ')
        print(commited.get('commit').get('author').get('name'))
