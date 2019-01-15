#!/usr/bin/env python3
import praw
import sys
import intrloop


new = False
limit = 10
reddit = praw.Reddit('bot1',user_agent='Script by /u/Sid299792')
for i,arg in enumerate(sys.argv):
    if arg == '-n':
        new = True
    elif arg == '-l':
        limit = int(sys.argv[i+1])

list_sub = []
if not new:
    list_sub = [submission for submission in reddit.subreddit('showerthoughts').hot(limit=limit)]
else:
    list_sub = [submission for submission in reddit.subreddit('showerthoughts').new(limit=limit)]

for i,submission in enumerate(list_sub):
    print(f"{i+1}.{submission.title}")

intrloop.loop(list_sub)

sys.exit(0)
