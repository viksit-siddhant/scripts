#!/usr/bin/env python3
import praw
import sys
import intrloop

new = False
limit = 10
nsfw = False
name_of_sub = input('name of sub-')
print('Fetching data...',end='')
reddit = praw.Reddit('bot1',user_agent='Script by /u/Sid299792')
for i,arg in enumerate(sys.argv):
    if arg == '-n':
        new = True
    elif arg == '-l':
        limit = int(sys.argv[i+1])
    elif arg == '-f':
        nsfw = True
def pull_from_sub(name_of_sub):
    list_sub = []
    params = {'include_over_18':'off'}
    if nsfw:
        params['include_over_18'] = "on"
    if not new:
         list_sub = list(reddit.subreddit(name_of_sub).hot(limit=limit,params=params))

    else:
        list_sub = list(reddit.subreddit(name_of_sub).new(limit=limit,params=params))
    return list_sub

list_sub = pull_from_sub(name_of_sub)
print('\r',end='')
for i,submission in enumerate(list_sub):
    print(f'{i+1}. {submission.title}\n')

intrloop.loop(list_sub)
sys.exit(0)
