a script for accessing subreddits, viewing their links, and reading comments, all from the command line. Run as `python intrloop.py [Options]`

dependencies:
    w3m
    praw

python version >= 3.6
Also, you need to register a script under the Reddit API and create a praw.ini file with your API key and secret.
For more information on how to do that, read the PRAW docs.

available options:
    `-f`      allow nsfw content
    `-n`      sort by new (default sorting is by hot)
    `-l`      set the number of posts to view (default is 10)

After you have run the script, enter the name of sub you want to browse and press Enter
