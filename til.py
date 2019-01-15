#!/usr/bin/env python3
import praw
import sys
import subprocess

new = False
limit = 10
nsfw = False
fltr = []
reddit = praw.Reddit('bot1',user_agent='Script by /u/Sid299792')
with open('filter','r') as f:
    for word in f.readlines():
        fltr.append(word[:-1])
for i,arg in enumerate(sys.argv):
    if arg == '-n':
        new = True
    elif arg == '-l':
        limit = int(sys.argv[i+1])
    elif arg == '-f':
        nsfw = True

list_sub = []
params = {'include_over_18':'off'}
if nsfw:
    params['include_over_18'] = "on"
if not new:
     list_sub = list(reddit.subreddit('todayilearned').hot(limit=limit,params=params))

else:
    list_sub = list(reddit.subreddit('todayilearned').new(limit=limit,params=params))

if not nsfw:
    for i,submission in enumerate(list_sub):
        sub_nsfw = False
        for word in fltr:
            if word in submission.title:
                sub_nsfw = True
                break
        if not sub_nsfw:
            print(f'{i+1}. {submission.title[3:]}\n')
else:
    for i,submission in enumerate(list_sub):
        print(f'{i+1}. {submission.title[3:]}\n')

num_of_link = 1
while True:
    a = input('>')
    if a == 'help':
        with open('help','r') as f:
            print(f.read())
    elif a == 'quit':
        break
    elif a == 'view':
        subprocess.run(['w3m',list_sub[num_of_link].url])
    elif a == 'comments':
        for i,comment in enumerate(list_sub[num_of_link].comments):
            print(comment.body)
            print('#'*100)
            if i == 5:
                break

    else:
        try:
            num_of_link = int(a) - 1
        except ValueError:
            print('Enter "help" for help')

sys.exit(0)
