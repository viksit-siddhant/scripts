import praw
import subprocess
import __main__

def loop(list_sub):
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
        elif a.split(' ')[0] == 'comments':
            lim_com = 5
            if len(a.split(' ')) > 1:
                lim_com = int(a.split(' ')[1])
            for i,comment in enumerate(list_sub[num_of_link].comments):
                print(comment.body)
                print('#'*100)
                if i+1 == lim_com:
                    break
        elif a.split(' ')[0] == 'change':
            list_sub = __main__.pull_from_sub(a.split(' ')[1])
            for i,submission in enumerate(list_sub):
                print(f'{i+1}. {submission.title}\n')

        else:
            try:
                num_of_link = int(a) - 1
            except ValueError:
                print('Enter "help" for help')
