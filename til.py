#!/usr/bin/env python3
import praw
import sys

new = False
limit = 10
reddit = praw.Reddit(client_id='ewfGJb9d_oD_Pg',
                     client_secret='2nb3H02fWJLzuTJ1_qWG_hErgno',
                     user_agent='Script by /u/Sid299792')

for i,arg in enumerate(sys.argv):
    if arg == '-n':
        new = True
    elif arg == '-l':
        limit = int(sys.argv[i+1])

if not new:
    for submission in reddit.subreddit('todayilearned').hot(limit=limit):
        print(submission.title + '\n')

else:
    for submission in reddit.subreddit('todayilearned').new(limit=limit):
        print(submission.title + '\n')

